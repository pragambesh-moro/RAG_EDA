import json
import re
import os

input_file = '../dataset.jsonl'
output_file = '../dataset_clean.jsonl'

def clean_instruction(text):
    # Remove things like "example 95 " or "example 95: " (case insensitive)
    text = re.sub(r'(?i)example\s+\d+[:\s]*', '', text)
    return text.strip()

def clean_output(text):
    # Replace shell prompts with newlines to format multi-command lines properly
    # Patterns to match: "prompt> ", "icc2_shell> ", "dc_shell> ", "pt_shell> ", "de_shell> "
    shells = [r'prompt>\s*', r'icc2_shell>\s*', r'dc_shell>\s*', r'pt_shell>\s*', r'de_shell>\s*']
    
    for shell in shells:
        text = re.sub(shell, '\n', text)
        
    # Clean up multiple newlines or leading/trailing whitespace
    text = '\n'.join([line.strip() for line in text.split('\n') if line.strip()])
    return text

def main():
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f if line.strip()]

    cleaned_data = []
    cleaned_count = 0

    for item in data:
        original_inst = item['instruction']
        original_out = item['output']
        
        new_inst = clean_instruction(original_inst)
        new_out = clean_output(original_out)
        
        if original_inst != new_inst or original_out != new_out:
            cleaned_count += 1
            
        cleaned_data.append({
            "instruction": new_inst,
            "output": new_out
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in cleaned_data:
            f.write(json.dumps(item) + "\n")

    print(f"Successfully cleaned {cleaned_count} dirty examples out of {len(data)} total.")
    print(f"Saved pristine base dataset to {output_file}")

if __name__ == "__main__":
    main()
