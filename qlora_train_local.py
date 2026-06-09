"""
qlora_train_local.py — QLoRA Fine-Tuning Optimised for RTX 4070 (8GB VRAM)
Hardware: Intel i9-13900HX | 32GB LPDDR5 | RTX 4070 8GB

Memory Strategy:
  - 4-bit NF4 quantisation + double quant   → model loads in ~3.5GB
  - Gradient checkpointing                  → trades VRAM for recomputation
  - paged_adamw_8bit                        → optimizer states page to CPU RAM
  - batch_size=1, grad_accum=16             → effective batch=16, minimal activations
  - bfloat16 compute                        → numerically stable on Ada Lovelace
  - max_memory cap                          → hard ceiling prevents CUDA OOM
  - PYTORCH_CUDA_ALLOC_CONF               → reduces fragmentation in the CUDA allocator

Quality is NOT compromised:
  - LoRA rank and alpha are unchanged (r=16, alpha=32)
  - Effective batch size is identical (16)
  - Same learning rate and number of training steps
  - Target modules expanded to k_proj too for richer gradient signal
  - Sequence length set to 256 (sufficient for all Tcl commands in dataset)
"""

import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import LoraConfig
from trl import SFTTrainer

# ─────────────────────────────────────────────
# Paths — update MODEL_ID to your local folder
# ─────────────────────────────────────────────
MODEL_ID = "./deepseek-coder-7b-base"   # local folder downloaded via download_hf_model.py
DATASET_PATH = "./dataset.jsonl"
OUTPUT_DIR = "./qlora-tcl-model-local"

# ─────────────────────────────────────────────
# CUDA Allocator Tuning (reduces fragmentation)
# Must be set before any CUDA calls
# ─────────────────────────────────────────────
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

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
    print("\n[1/5] Loading dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
    print(f"      {len(dataset):,} training examples loaded.")

    # ── Tokenizer ──────────────────────────────────────────────
    print("\n[2/5] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"   # Required for causal LM training

    # ── Quantisation Config ────────────────────────────────────
    print("\n[3/5] Configuring 4-bit quantisation...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",              # NormalFloat4 — optimal for LLM weights
        bnb_4bit_compute_dtype=torch.bfloat16,  # bf16 is stable on Ada Lovelace (RTX 40xx)
        bnb_4bit_use_double_quant=True,         # Quantise the quantisation constants too (~0.4 bits saved)
    )

    # Hard cap: leave ~1GB headroom for activations and CUDA kernels
    max_memory = {0: "7GB", "cpu": "28GB"}      # GPU cap 7GB, rest pages to 28GB RAM

    print("\n[4/5] Loading model into GPU...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map="auto",
        max_memory=max_memory,
    )

    # Gradient checkpointing: recomputes activations during backward pass
    # instead of storing them — trades ~20% speed for ~40% VRAM saving
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # ── LoRA Config ────────────────────────────────────────────
    # Expanded target_modules to include k_proj for richer adapter coverage
    # This adds minimal VRAM overhead but improves the quality of gradient updates
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj"],  # Added k_proj vs HPC version
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── Training Arguments ─────────────────────────────────────
    print("\n[5/5] Setting training arguments...")
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,

        # Memory: batch=1 is the only safe option for 8GB VRAM.
        # Effective batch = batch_size × grad_accum = 1 × 16 = 16 (identical to HPC)
        per_device_train_batch_size=1,
        gradient_accumulation_steps=16,

        # Gradient checkpointing frees activation VRAM during forward pass
        gradient_checkpointing=True,

        # Quality hyperparameters — identical to HPC version
        learning_rate=2e-4,
        lr_scheduler_type="cosine",    # Cosine decay is smoother than linear for adapters
        warmup_ratio=0.05,             # 5% warmup steps prevent early instability
        max_steps=500,
        logging_steps=10,
        save_steps=100,
        save_total_limit=2,            # Keep only last 2 checkpoints to save disk space

        # Precision: bf16 on RTX 4070 (Ada Lovelace has native bf16 tensor cores)
        bf16=True,
        fp16=False,

        # Optimizer: paged version pages optimizer state to 28GB system RAM
        # This is the key trick that makes 7B QLoRA feasible on 8GB VRAM
        optim="paged_adamw_8bit",

        # DataLoader: use i9's E-cores for parallel data prefetching
        dataloader_num_workers=4,
        dataloader_pin_memory=True,    # Pre-pin batches in RAM for faster GPU transfer

        report_to="none",              # Disable wandb/tensorboard unless you want it
    )

    # ── Trainer ────────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        formatting_func=lambda batch: [
            format_instruction({"instruction": i, "output": o})
            for i, o in zip(batch["instruction"], batch["output"])
        ],
        max_seq_length=256,            # Tcl commands are short; 256 tokens is sufficient
        tokenizer=tokenizer,
        args=training_args,
    )

    # ── Run ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("Starting QLoRA Fine-Tuning on RTX 4070...")
    print(f"  Effective batch size : {training_args.per_device_train_batch_size * training_args.gradient_accumulation_steps}")
    print(f"  Max steps            : {training_args.max_steps}")
    print(f"  Output directory     : {OUTPUT_DIR}")
    print("=" * 60 + "\n")

    trainer.train()

    # ── Save ───────────────────────────────────────────────────
    print(f"\nSaving LoRA adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print("\nDone! Adapters saved. Run inference with peft's merge_and_unload().")


if __name__ == "__main__":
    main()
