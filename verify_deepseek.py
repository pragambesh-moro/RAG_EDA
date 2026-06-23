from transformers import AutoConfig, AutoTokenizer

model_path = "./deepseek-coder-7b-base"

try:
    print("Verifying configuration and tokenizer...")
    config = AutoConfig.from_pretrained(model_path, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    print("✅ Success! Local model files are valid and ready for training.")
except Exception as e:
    print(f"❌ Verification failed: {e}")