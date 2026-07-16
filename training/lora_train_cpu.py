"""
lora_train_cpu.py — CPU-Optimised LoRA Fine-Tuning for AMD Threadripper
Hardware: AMD Ryzen Threadripper PRO 7945WX | 256GB RAM
"""

import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    PreTrainedTokenizerFast,
)
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

MODEL_ID = "deepseek-ai/deepseek-coder-6.7b-base"
DATASET_PATH = "./dataset_clean.jsonl"
OUTPUT_DIR = "./lora-tcl-model-cpu"

os.environ["PYTHONUTF8"] = "1"

def format_instruction(example: dict) -> str:
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )

def main():
    print("=" * 60)
    print("LoRA CPU Training — Threadripper Optimised")
    print("=" * 60)

    print("\n[1/5] Loading and formatting dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")

    dataset = dataset.map(
        lambda example: {"text": format_instruction(example)},
        remove_columns=dataset.column_names,
    )
    print(f"      {len(dataset):,} training examples loaded.")

    print("\n[2/5] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = "<｜end▁of▁sentence｜>"
    tokenizer.eos_token = "<｜end▁of▁sentence｜>"
    tokenizer.bos_token = "<｜begin▁of▁sentence｜>"
    tokenizer.padding_side = "right"

    print("\n[3/5] Loading model onto CPU in native bfloat16...")
    # Load in bfloat16 to leverage Zen 4 AVX-512 BF16 instructions natively!
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="cpu",
        torch_dtype=torch.bfloat16,
    )
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    print("\n[4/5] Applying LoRA Adapters...")
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    print("\n[5/5] Setting CPU training arguments...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        use_cpu=True,                  # Force CPU usage
        per_device_train_batch_size=1, # Keep memory footprint low
        gradient_accumulation_steps=16,
        gradient_checkpointing=True,
        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_steps=25,
        max_steps=500,
        logging_steps=10,
        save_steps=100,
        save_total_limit=2,
        max_length=512,                # Optimal sequence length for single-command generation
        dataset_text_field="text",
        bf16=True,                     # Native BF16 acceleration
        fp16=False,
        optim="adamw_torch",           # Removed 8bit optimizer since no CUDA
        dataloader_num_workers=4,
        dataloader_pin_memory=False,   # No pinned memory needed for CPU
        report_to="none",
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        processing_class=tokenizer,
        args=training_args,
    )

    print("\n" + "=" * 60)
    print("Starting CPU LoRA Fine-Tuning...")
    print(f"  Target             : Threadripper PRO 7945WX")
    print(f"  Max sequence length: {training_args.max_length}")
    print(f"  Output directory   : {OUTPUT_DIR}")
    print("=" * 60 + "\n")

    trainer.train()

    print(f"\nSaving LoRA adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("\nDone!")

if __name__ == "__main__":
    main()
