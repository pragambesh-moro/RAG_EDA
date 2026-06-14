import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, PreTrainedTokenizerFast, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

MODEL_ID = "/scratch/pm944/deepseek-coder-7b-base"
DATASET_PATH = "/scratch/pm944/dataset.jsonl"
OUTPUT_DIR = "/scratch/pm944/qlora-tcl-model-backup"

def format_instruction(example: dict) -> str:
    return (
        f"### Instruction:\n{example['instruction']}\n\n"
        f"### Response:\n{example['output']}"
    )

def main():
    # ── 1. Dataset ──────────────────────────────────────────────
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
    dataset = dataset.map(
        lambda example: {"text": format_instruction(example)},
        remove_columns=dataset.column_names,
    )

    # ── 2. Tokenizer ────────────────────────────────────────────
    tokenizer_file = os.path.join(MODEL_ID, "tokenizer.json")
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=tokenizer_file)
    tokenizer.pad_token = "<｜end▁of▁sentence｜>"
    tokenizer.eos_token = "<｜end▁of▁sentence｜>"
    tokenizer.bos_token = "<｜begin▁of▁sentence｜>"
    tokenizer.padding_side = "right"

    # ── 3. 4-Bit Quantization Configuration ──────────────────────
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.float16, # float16 is safer for MIG standard compliance
    )
    
    # device_map allocation handled automatically by torchrun/DDP
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    device_map = {"": local_rank}

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map=device_map,
    )
    model.config.use_cache = False
    model.gradient_checkpointing_enable()

    # ── 4. Squeezed LoRA Configuration ──────────────────────────
    # Clamped to r=16 and attention blocks only to fit 10GB per slice limit
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # ── 5. Training Arguments ───────────────────────────────────
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        per_device_train_batch_size=1,        # Essential: 1 sequence per slice to avoid OOM
        gradient_accumulation_steps=32,       # 32 steps * 2 GPUs = Effective Batch Size of 64
        gradient_checkpointing=True,
        
        # Quick run check: 500 steps instead of full epochs
        max_steps=500,
        num_train_epochs=-1,

        learning_rate=2e-4,
        lr_scheduler_type="cosine",
        warmup_ratio=0.05,
        logging_steps=10,
        save_strategy="steps",
        save_steps=250,
        save_total_limit=1,

        max_length=256,                       # Clamped context to protect dynamic VRAM spikes
        dataset_text_field="text",
        
        fp16=True,                            # Use standard fp16 for slice isolation
        bf16=False,
        optim="paged_adamw_8bit",             # Offloads optimizer states to host RAM
        
        ddp_find_unused_parameters=False,     # Standard DDP speedup flag
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

    # Only print stats on the primary process loop to avoid spamming console logs
    if local_rank == 0:
        print(f"Executing on 2 MIG Slices via Distributed Data Parallel...")
        print(f"Max Context Length Set to: {training_args.max_length}")

    trainer.train()

    if local_rank == 0:
        print(f"Saving backup adapters to {OUTPUT_DIR}...")
        trainer.model.save_pretrained(OUTPUT_DIR)
        tokenizer.save_pretrained(OUTPUT_DIR)
        print("Backup training run successful!")

if __name__ == "__main__":
    main()