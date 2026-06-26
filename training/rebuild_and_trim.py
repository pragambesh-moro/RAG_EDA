import os
os.environ["PYTHONUTF8"] = "1"

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# Pulling the base directly from Hugging Face
BASE_MODEL = "deepseek-ai/deepseek-coder-7b-base"
# The backup you saved
LORA_DIR = "./lora-export-clean-amd"
# The new, clean output
OUT_DIR = "./merged-synopsys-7b-trimmed"

print("1. Downloading & Loading Base Model (Go grab a coffee, this is ~14GB)...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL, 
    torch_dtype=torch.float16, 
    device_map="cpu", 
    trust_remote_code=True
)

print(f"\n2. Chopping the fat... (Vocab size: {len(tokenizer)} | Tensor size: {base_model.config.vocab_size})")
base_model.resize_token_embeddings(len(tokenizer))

print("3. Fusing your Synopsys LoRA adapter...")
model = PeftModel.from_pretrained(base_model, LORA_DIR)
merged_model = model.merge_and_unload()

print(f"4. Saving the pristine, trimmed model to {OUT_DIR}...")
merged_model.save_pretrained(OUT_DIR)
tokenizer.save_pretrained(OUT_DIR)

print("\nRebuild complete! Ready for conversion.")
