import os
import json
from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter

def semantic_chunk_markdowns(input_dir: str, output_file: str):
    # Define the headers we want to split on
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3")
    ]
    
    # Initialize the LangChain text splitter
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False # Keep the headers in the content for LLM context
    )
    
    md_paths = list(Path(input_dir).glob("*.md"))
    if not md_paths:
        print(f"No Markdown files found in {input_dir}")
        return

    all_chunks = []
    
    for md_path in md_paths:
        print(f"Chunking {md_path.name}...")
        
        try:
            content = md_path.read_text(encoding="utf-8")
            
            # This handles all the semantic splitting while preserving tables and arguments!
            splits = markdown_splitter.split_text(content)
            
            for split in splits:
                # Add source document info to metadata
                split.metadata["Source"] = md_path.name
                
                # Convert the LangChain Document object into a clean dictionary
                chunk_data = {
                    "metadata": split.metadata,
                    "content": split.page_content
                }
                all_chunks.append(chunk_data)
                
        except Exception as e:
            print(f"Failed to process {md_path.name}: {e}")

    # Export to JSONL format
    print(f"Writing {len(all_chunks)} semantic chunks to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + '\n')
            
    print("Done! Ready for Phase 3.")

if __name__ == "__main__":
    INPUT_DIRECTORY = "./parsed_markdown"
    OUTPUT_JSONL = "./semantic_chunks.jsonl"
    
    semantic_chunk_markdowns(INPUT_DIRECTORY, OUTPUT_JSONL)
