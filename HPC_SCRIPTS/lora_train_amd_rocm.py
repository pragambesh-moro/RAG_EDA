"""
lora_train_amd_rocm.py — Pure LoRA Fine-Tuning for AMD Instinct MI300X
Fixed: NaN gradients, attention instabilities, and disconnected graphs.
"""

import os
import torch

# ── ROCm / MI300X Hardware Stability Flags ──────────────────
# 1. Target MI300X architecture explicitly (CDNA3)
os.environ["HSA_OVERRIDE_GFX_VERSION"] = "9.4.2"

# 2. ENABLE hipBLASLt! Disabling this kills your TFLOPs and forces legacy BLAS.
# We fix the NaN issues structurally below, so we want the high-speed matrix cores ON.
os.environ["TORCH_BLAS_PREFER_HIPBLASLT"] = "1"

# 3. Prevent HSA memory fragmentation over long runs
os.environ["PYTORCH_HIP_ALLOC_CONF"] = "expandable_segments:True"

from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig
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
    print("AMD MI300X Pure LoRA Training - Optimized")
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
    print("\n[2/4] Loading AutoTokenizer...")
    # FIX: Use AutoTokenizer instead of raw PreTrainedTokenizerFast 
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # ── 3. Model Loading (Pure bfloat16 + SDPA) ─────────────────
    print("\n[3/4] Loading model in pure bfloat16...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map={"":  0}, 
        attn_implementation="sdpa", # FIX: Force SDPA to prevent FlashAttention-2 ROCm bugs
        trust_remote_code=True
    )
    model.config.use_cache = False

    # FIX: Upcast RMSNorm layers to float32!
    # Pure bf16 normalization variance calculation often underflows, causing instant NaNs.
    for name, module in model.named_modules():
        if "norm" in name.lower():
            module.to(torch.float32)

    # FIX: Ensure gradients flow correctly from LoRA adapters to inputs
    # This solves the "disconnected graph" bug in PEFT.
    if hasattr(model, "enable_input_require_grads"):
        model.enable_input_require_grads()

    # ── 4. LoRA Configuration ───────────────────────────────────
    lora_config = LoraConfig(
        r=64,
        lora_alpha=64,             
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        lora_dropout=0.0,          # Kept at 0.0: ROCm HIP dropout kernel is unsafe with bf16
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── 5. Training Config ──────────────────────────────────────
    print("\n[4/4] Setting training arguments...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,   
        num_train_epochs=5,              
        max_steps=-1,
        learning_rate=2e-5,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        max_grad_norm=1.0,               # Relaxed to 1.0 since FP32 Norm solves the instability

        # FIX: We can safely use checkpointing now to save VRAM
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},

        logging_steps=5,
        save_strategy="epoch",

        max_seq_length=1024,             # FIX: SFTConfig expects max_seq_length, not max_length
        dataset_text_field="text",

        bf16=True,
        fp16=False,

        optim="adamw_torch",             
        weight_decay=0.01,

        dataloader_num_workers=4,
        dataloader_pin_memory=False,     
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

    trainable = sum(p.numel() for p in trainer.model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in trainer.model.parameters())
    print(f"\n  Trainable parameters: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

    # ── Gradient health check ───────────────────────────────────
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
        print("  WARNING: NaN detected in gradients during sanity check!")
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