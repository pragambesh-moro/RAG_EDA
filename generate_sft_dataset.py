import json
import re

def generate_synthetic_dataset(input_jsonl: str, output_jsonl: str):
    print("Parsing semantic chunks for Tcl commands...")
    dataset = []
    
    with open(input_jsonl, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            content = data.get("content", "")
            metadata = data.get("metadata", {})
            
            # Find all markdown code blocks (e.g., ``` ... ```)
            code_blocks = re.findall(r'```(?:tcl)?\n(.*?)\n```', content, re.DOTALL)
            
            for code in code_blocks:
                code = code.strip()
                # Heuristic: Valid Tcl commands typically have flags (-) and snake_case names (_)
                if '-' in code and '_' in code:
                    # Strip away interactive shell prompts (e.g., ptc_shell>, icc2_shell>)
                    clean_code = re.sub(r'^[a-zA-Z0-9_]+>\s*', '', code, flags=re.MULTILINE)
                    
                    # Synthesize an instruction from the Markdown Headers!
                    header_context = metadata.get("Header 2", metadata.get("Header 1", "this task"))
                    instruction = f"Write the Tcl command for {header_context.lower()}."
                    
                    dataset.append({
                        "instruction": instruction,
                        "output": clean_code
                    })

    # Deduplicate exact matches
    unique_dataset = {json.dumps(d, sort_keys=True): d for d in dataset}.values()
    
    print(f"Successfully synthesized {len(unique_dataset)} unique instruction-output pairs via heuristics.")
    
    with open(output_jsonl, 'w', encoding='utf-8') as out:
        for item in unique_dataset:
            out.write(json.dumps(item) + "\n")
            
    print(f"Saved local dataset to {output_jsonl}. Ready to transfer to HPC!")

if __name__ == "__main__":
    INPUT_JSONL = "./semantic_chunks.jsonl"
    OUTPUT_JSONL = "./dataset.jsonl"
    generate_synthetic_dataset(INPUT_JSONL, OUTPUT_JSONL)
