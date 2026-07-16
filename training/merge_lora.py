"""
merge_lora.py — Fuses LoRA adapters with the base model into a single PyTorch model.
"""

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

BASE_MODEL = "deepseek-ai/deepseek-coder-6.7b-base"
LORA_ADAPTERS = "D:\Research\RAG_EDA\lora-tcl-model-cpu"  # Path to your trained adapters
OUTPUT_DIR = "./merged_model_cpu"

def main():
    print("=" * 60)
    print("Fusing LoRA Adapters into Base Model...")
    print("=" * 60)
    
    print("\n[1/4] Loading Base Model in fp16...")
    # Loading in fp16 keeps the RAM footprint under 14GB so it doesn't crash
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16,
        device_map="cpu",
        low_cpu_mem_usage=True
    )
    
    print("\n[2/4] Loading Tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(LORA_ADAPTERS)
    
    print("\n[3/4] Applying LoRA Adapters...")
    model = PeftModel.from_pretrained(base_model, LORA_ADAPTERS)
    
    print("      Fusing weights together (This might take a minute)...")
    model = model.merge_and_unload()
    
    print(f"\n[4/4] Saving massive merged model to {OUTPUT_DIR}...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    model.save_pretrained(OUTPUT_DIR, safe_serialization=True)
    tokenizer.save_pretrained(OUTPUT_DIR)
    
    print("\nDone! The model is now ready for llama.cpp conversion.")

if __name__ == "__main__":
    main()
