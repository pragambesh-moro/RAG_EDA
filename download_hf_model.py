import os
from huggingface_hub import snapshot_download

# This is the 7 Billion parameter Code LLM we will fine-tune
model_id = "deepseek-ai/deepseek-coder-7b-base"
local_dir = "./deepseek-coder-7b-base"

print(f"Downloading {model_id} locally to {local_dir}...")
print("This will pull approximately 14GB of weights. Please wait...")

# snapshot_download downloads the entire repository
# We ignore msgpack and h5 weights as we only need the safetensors/pytorch bins
snapshot_download(
    repo_id=model_id, 
    local_dir=local_dir, 
    ignore_patterns=["*.msgpack", "*.h5", "*.ot"]
)

print("==================================================")
print(f"Download complete! ")
print(f"1. SCP the entire '{local_dir}' folder to your HPC.")
print(f"2. Update MODEL_ID in qlora_train.py to point to the uploaded folder path.")
print("==================================================")
