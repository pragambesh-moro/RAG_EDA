import os
os.environ["PYTHONUTF8"] = "1"
from transformers import AutoTokenizer

print("Downloading clean tokenizer...")
t = AutoTokenizer.from_pretrained('deepseek-ai/deepseek-coder-7b-base', trust_remote_code=True)
print("Saving tokenizer with pristine UTF-8 encoding...")
t.save_pretrained('./merged-synopsys-7b-trimmed')
print("Done!")
