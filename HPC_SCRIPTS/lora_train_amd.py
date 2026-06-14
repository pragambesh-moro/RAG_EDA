"""
lora_train_amd.py — Pure LoRA Fine-Tuning for AMD Instinct MI300X (192GB VRAM)

No Quantization. No Gradient Checkpointing. No BitsAndBytes.
Pure bfloat16 training utilizing the massive memory and compute of the MI300X.
"""

import os
import torch

# ── ROCm Stability ──────────────────────────────────────────
# Prevent NaN from hipBLASLt GEMM kernels during optimizer steps
os.environ["TORCH_BLAS_PREFER_HIPBLASLT"] = "0"
# Use expandable memory segments for stable HIP memory allocation
os.environ["PYTORCH_HIP_ALLOC_CONF"] = "expandable_segments:True"

from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    PreTrainedTokenizerFast,
)
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

MODEL_ID = "./deepseek-coder-7b-base"
DATASET_PATH = "./dataset.jsonl"
OUTPUT_DIR = "./lora-tcl-model-amd"

def format_instruction(example: dict) -> str:
    """Formats a single instruction-output pair into a training string."""
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )

def main():
    print("=" * 60)
    print("AMD MI300X Pure LoRA Training")
    print("=" * 60)

    # ── 1. Dataset ──────────────────────────────────────────────
    print("\n[1/4] Loading dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
    dataset = dataset.map(
        lambda example: {"text": format_instruction(example)},
        remove_columns=dataset.column_names,
    )
    print(f"      {len(dataset)} training examples loaded.")

    # ── 2. Tokenizer ────────────────────────────────────────────
    print("\n[2/4] Loading fast tokenizer...")
    # Load directly from tokenizer.json to avoid the HF AutoTokenizer space-stripping bug
    tokenizer_file = os.path.join(MODEL_ID, "tokenizer.json")
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=tokenizer_file)
    tokenizer.pad_token = "<｜end▁of▁sentence｜>"
    tokenizer.eos_token = "<｜end▁of▁sentence｜>"
    tokenizer.bos_token = "<｜begin▁of▁sentence｜>"
    tokenizer.padding_side = "right"

    # ── 3. Model Loading (Pure bfloat16) ────────────────────────
    print("\n[3/4] Loading model in pure bfloat16 (no quantization)...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map={"":  0},  # "auto" is for inference — breaks gradient flow in PEFT training
    )
    model.config.use_cache = False

    # NOTE: We intentionally do NOT use gradient_checkpointing_enable().
    # With 192GB VRAM we have ~150GB of headroom for a 7B model.
    # Gradient checkpointing + Pure LoRA on ROCm causes NaN gradients
    # due to a disconnected computational graph.

    # ── 4. LoRA Configuration ───────────────────────────────────
    lora_config = LoraConfig(
        r=64,
        lora_alpha=64,             # scaling = alpha/r = 1.0  (was 2.0 — caused bf16 overflow)
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        lora_dropout=0.0,          # ROCm HIP dropout kernel produces NaN with bf16
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── 5. Training Config ──────────────────────────────────────
    print("\n[4/4] Setting training arguments...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,

        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,   # Effective batch = 32

        num_train_epochs=5,              # More epochs for a small 830-example dataset
        max_steps=-1,

        learning_rate=2e-5,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        max_grad_norm=0.3,               # Tighter clipping for ROCm bf16 stability

        logging_steps=5,
        save_strategy="epoch",

        max_length=1024,                 # Our Tcl examples are short; no need for 4096
        dataset_text_field="text",

        bf16=True,
        fp16=False,

        optim="adamw_torch",
        weight_decay=0.01,

        dataloader_num_workers=4,
        dataloader_pin_memory=False,     # pin_memory causes memory faults on ROCm
        report_to="none",
    )

    # ── 6. Execution ────────────────────────────────────────────
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,
        processing_class=tokenizer,
        args=training_args,
    )

    # Sanity check: verify gradients are flowing
    trainable = sum(p.numel() for p in trainer.model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in trainer.model.parameters())
    print(f"\n  Trainable parameters: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

    # ── Gradient health check ───────────────────────────────────
    # Run a single forward+backward pass to catch NaN before wasting a full run
    print("  Running gradient sanity check...")
    sample = next(iter(trainer.get_train_dataloader()))
    sample = {k: v.to(trainer.model.device) for k, v in sample.items()}
    outputs = trainer.model(**sample)
    outputs.loss.backward()
    has_nan = any(
        p.grad is not None and torch.isnan(p.grad).any()
        for p in trainer.model.parameters()
    )
    trainer.model.zero_grad()
    if has_nan:
        print("  ⚠ WARNING: NaN detected in gradients during sanity check!")
        print("    Training will likely fail. Check model/data/config.")
    else:
        print("  ✓ Gradient sanity check passed — no NaN detected.")

    print(f"  Beginning Pure LoRA fine-tuning...\n")
    trainer.train()

    print(f"\nSaving AMD LoRA adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Training run successful!")

if __name__ == "__main__":
    main()
