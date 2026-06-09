"""
qlora_train_hpc_full.py — QLoRA Fine-Tuning for HPC (Full A100 80GB)

Upgrades over the local/MIG version:
  - Full A100 80GB (no VRAM pressure → larger batch, longer sequences)
  - LoRA rank r=64 (4x more expressive adapters)
  - All 7 target modules (attention + MLP) instead of just q/v
  - 3 full epochs over the dataset instead of 500 steps
  - Sequence length 1024 (captures long Tcl command blocks)
  - Larger per-device batch (8) for faster convergence
"""

import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)
from peft import LoraConfig, prepare_model_for_kbit_training
from trl import SFTTrainer, SFTConfig

# ─────────────────────────────────────────────
# Paths — update to your HPC scratch directory
# ─────────────────────────────────────────────
MODEL_ID = "/scratch/pm944/deepseek-coder-7b-base"
DATASET_PATH = "/scratch/pm944/dataset.jsonl"
OUTPUT_DIR = "/scratch/pm944/qlora-tcl-model-full"


def format_instruction(example: dict) -> str:
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )


def main():
    print("=" * 60)
    print("QLoRA HPC Training — Full A100 80GB")
    print("=" * 60)

    # ── Dataset ────────────────────────────────────────────────
    print("\n[1/4] Loading and formatting dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
    dataset = dataset.map(
        lambda example: {"text": format_instruction(example)},
        remove_columns=dataset.column_names,
    )
    print(f"      {len(dataset):,} training examples loaded.")

    # ── Tokenizer ──────────────────────────────────────────────
    print("\n[2/4] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # ── Model ──────────────────────────────────────────────────
    print("\n[3/4] Loading model into GPU...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,  # bfloat16: numerically stable, A100 native
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map="auto",
    )
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # ── LoRA Config ────────────────────────────────────────────
    # Full coverage: attention (q/k/v/o) + MLP (gate/up/down)
    # r=64 gives 4x more adapter expressiveness vs the MIG version (r=16)
    # lora_alpha = 2×r is standard scaling practice
    lora_config = LoraConfig(
        r=64,
        lora_alpha=128,
        target_modules=[
            # Attention projections
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            # MLP / Feed-Forward layers
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── Training Config ────────────────────────────────────────
    print("\n[4/4] Setting training arguments...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,

        # 80GB allows batch=8; combined with grad_accum=8 → effective batch = 64
        per_device_train_batch_size=8,
        gradient_accumulation_steps=8,
        gradient_checkpointing=True,

        # Train for 3 full epochs over all 5,903 examples
        # (more principled than a fixed step count)
        num_train_epochs=3,
        max_steps=-1,           # -1 means use num_train_epochs instead

        learning_rate=1e-4,     # Slightly lower LR for larger rank adapters (more stable)
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,

        logging_steps=20,
        save_strategy="epoch",  # Save a checkpoint after every epoch
        save_total_limit=3,

        max_length=1024,        # Full sequences — captures long Tcl command blocks
        dataset_text_field="text",

        bf16=True,              # A100 has native bf16 tensor cores
        fp16=False,
        tf32=True,              # Additional free speedup on A100

        optim="paged_adamw_8bit",
        dataloader_num_workers=8,
        dataloader_pin_memory=True,

        report_to="none",
    )

    # ── Trainer ────────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        processing_class=tokenizer,
        args=training_args,
    )

    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"\n  Trainable parameters  : {total_params:,}")
    print(f"  Effective batch size  : {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps}")
    print(f"  Epochs                : {training_args.num_train_epochs}")
    print(f"  Sequence length       : {training_args.max_length}")
    print(f"  LoRA rank             : {lora_config.r}")
    print(f"  Target modules        : {lora_config.target_modules}")
    print(f"  Output                : {OUTPUT_DIR}\n")

    trainer.train()

    print(f"\nSaving LoRA adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Done!")


if __name__ == "__main__":
    main()
