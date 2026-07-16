import json
import random
import os

input_file = '../dataset_clean.jsonl'
output_file = '../dataset_v2.jsonl'
num_synthetic_examples = 300

def main():
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # Read original single-command data
    with open(input_file, 'r', encoding='utf-8') as f:
        original_data = [json.loads(line) for line in f if line.strip()]

    print(f"Loaded {len(original_data)} original examples.")

    synthetic_data = []
    
    # Generate multi-step examples
    for _ in range(num_synthetic_examples):
        # Randomly choose between 3 to 6 steps to simulate a long flow script
        num_steps = random.randint(3, 6)
        selected_pairs = random.sample(original_data, num_steps)
        
        instructions = []
        outputs = []
        
        for i, pair in enumerate(selected_pairs):
            # Clean up the original instructions so they flow naturally in a paragraph
            inst = pair['instruction'].replace("Write the Tcl command for ", "").replace("Write the Tcl command to ", "").strip()
            # Ensure it ends with a period
            if not inst.endswith('.'):
                inst += '.'
            
            # Add sequential transition words
            if i == 0:
                instructions.append(f"Write a complete script that does the following: First, {inst}")
            elif i == num_steps - 1:
                instructions.append(f"Finally, {inst}")
            else:
                instructions.append(f"Then, {inst}")
                
            outputs.append(pair['output'])
            
        full_instruction = " ".join(instructions)
        full_output = "\n".join(outputs)
        
        synthetic_data.append({
            "instruction": full_instruction,
            "output": full_output
        })

    # Write the new combined dataset
    with open(output_file, 'w', encoding='utf-8') as f:
        # 1. Write the original data so it doesn't forget how to do single commands
        for item in original_data:
            f.write(json.dumps(item) + "\n")
            
        # 2. Append the synthetic multi-step data to cure length-collapse
        for item in synthetic_data:
            f.write(json.dumps(item) + "\n")

    print(f"Generated {num_synthetic_examples} multi-step examples.")
    print(f"Saved combined dataset ({len(original_data) + num_synthetic_examples} total) to {output_file}")

if __name__ == "__main__":
    main()
