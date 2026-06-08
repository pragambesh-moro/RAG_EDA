import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

# Base Model - UPDATE THIS PATH to your scratch directory on the HPC
# e.g., MODEL_ID = "/scratch/pm944/deepseek-coder-7b-base"
MODEL_ID = "deepseek-ai/deepseek-coder-7b-base"
DATASET_PATH = "dataset.jsonl"
OUTPUT_DIR = "./qlora-tcl-model"

def format_instruction(example):
    """Formats the instruction and output into a single string for the model to learn."""
    return f"### Instruction:\n{example['instruction']}\n\n### Response:\n{example['output']}"

def main():
    print("Loading Dataset...")
    dataset = load_dataset("json", data_files=DATASET_PATH, split="train")

    print("Loading Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token

    print("Loading Model in 4-bit (QLoRA)...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,     # Saves an additional ~0.4 bits per param
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,     # Correct modern API (not load_in_4bit=True directly)
        device_map="auto",
    )

    # Prepare model for PEFT (disables caching, enables gradient checkpointing)
    model = prepare_model_for_kbit_training(model)

    print("Configuring LoRA...")
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )

    # BUG FIX 1: Apply LoRA to model manually OR let SFTTrainer do it via peft_config.
    # Doing BOTH causes LoRA to be applied twice. We let SFTTrainer handle it.
    # model = get_peft_model(model, lora_config)  <-- REMOVED

    print("Setting Training Arguments...")
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=10,
        max_steps=500,
        save_steps=100,
        fp16=True,
        optim="paged_adamw_8bit"
    )

    print("Initializing SFT Trainer...")
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=lora_config,            # SFTTrainer applies LoRA internally
        # BUG FIX 2: formatting_func receives a BATCH (dict of lists), not a single example.
        # We zip the batch fields together to iterate over individual examples.
        formatting_func=lambda batch: [
            format_instruction({"instruction": i, "output": o})
            for i, o in zip(batch["instruction"], batch["output"])
        ],
        max_seq_length=512,
        # BUG FIX 3: Removed dataset_text_field="text" — our dataset has no "text" field.
        # It conflicts with formatting_func and caused a silent key error.
        tokenizer=tokenizer,
        args=training_args,
    )

    print("Starting QLoRA Fine-Tuning!")
    trainer.train()

    print(f"Saving Fine-Tuned Adapters to {OUTPUT_DIR}...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

if __name__ == "__main__":
    main()
