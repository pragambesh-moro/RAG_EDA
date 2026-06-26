"""
qlora_train_local.py — QLoRA Fine-Tuning Optimised for RTX 4070 (8GB VRAM)
Hardware: Intel i9-13900HX | 32GB LPDDR5 | RTX 4070 8GB
"""

import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    PreTrainedTokenizerFast,
    BitsAndBytesConfig,
)
from peft import LoraConfig, prepare_model_for_kbit_training
from trl import SFTTrainer, SFTConfig

# ─────────────────────────────────────────────
# Paths — update MODEL_ID to your local folder
# ─────────────────────────────────────────────
MODEL_ID = "./deepseek-coder-7b-base"
DATASET_PATH = "./dataset.jsonl"
OUTPUT_DIR = "./qlora-tcl-model-local"

# ─────────────────────────────────────────────
# CUDA Allocator Tuning
# ─────────────────────────────────────────────
os.environ["PYTHONUTF8"] = "1"   # Prevent Windows encoding errors in trl

# TF32 acceleration on Ada Lovelace (RTX 40 series) — free speedup, no quality loss
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True


def format_instruction(example: dict) -> str:
    """Formats a single instruction-output pair into a training string."""
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )


def main():
    print("=" * 60)
    print("QLoRA Local Training — RTX 4070 Optimised")
    print("=" * 60)

    # ── Dataset ────────────────────────────────────────────────
    print("\n[1/5] Loading and formatting dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")

    # Pre-process dataset to add a "text" column.
    # This is the stable approach across all TRL versions — avoids formatting_func API churn.
    dataset = dataset.map(
        lambda example: {"text": format_instruction(example)},
        remove_columns=dataset.column_names,
    )
    print(f"      {len(dataset):,} training examples loaded.")

    # ── Tokenizer ──────────────────────────────────────────────
    print("\n[2/5] Loading tokenizer...")
    tokenizer_file = os.path.join(MODEL_ID, "tokenizer.json")
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=tokenizer_file)
    tokenizer.pad_token = "<｜end▁of▁sentence｜>"
    tokenizer.eos_token = "<｜end▁of▁sentence｜>"
    tokenizer.bos_token = "<｜begin▁of▁sentence｜>"
    tokenizer.padding_side = "right"

    # ── Quantisation Config ────────────────────────────────────
    print("\n[3/5] Configuring 4-bit quantisation...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    # Hard cap: leave ~1GB headroom for activations and CUDA kernels
    max_memory = {0: "7GB", "cpu": "28GB"}

    print("\n[4/5] Loading model into GPU...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map="auto",
        max_memory=max_memory,
    )
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # ── LoRA Config ────────────────────────────────────────────
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── SFTConfig (Training Arguments) ────────────────────────
    print("\n[5/5] Setting training arguments...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,
        gradient_checkpointing=True,
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_steps=25,
        max_steps=500,
        logging_steps=10,
        save_steps=100,
        save_total_limit=2,
        max_length=256,                # Sequence length cap (SFTConfig parameter)
        dataset_text_field="text",     # Column name we created in pre-processing
        bf16=True,
        fp16=False,
        optim="paged_adamw_8bit",
        dataloader_num_workers=4,
        dataloader_pin_memory=True,
        report_to="none",
    )

    # ── Trainer ────────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        processing_class=tokenizer,    # 'tokenizer' was renamed to 'processing_class' in TRL >= 0.12
        args=training_args,
    )

    print("\n" + "=" * 60)
    print("Starting QLoRA Fine-Tuning on RTX 4070...")
    print(f"  Effective batch size : {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps}")
    print(f"  Max steps            : {training_args.max_steps}")
    print(f"  Output directory     : {OUTPUT_DIR}")
    print("=" * 60 + "\n")

    trainer.train()

    print(f"\nSaving LoRA adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("\nDone!")


if __name__ == "__main__":
    main()
