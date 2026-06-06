import os
from pathlib import Path
from docling.document_converter import DocumentConverter

def batch_convert_manuals(pdf_directory: str, output_directory: str):
    # Initialize the layout-aware parser
    converter = DocumentConverter()
    pdf_paths = list(Path(pdf_directory).glob("*.pdf"))
    
    os.makedirs(output_directory, exist_ok=True)
    
    for pdf in pdf_paths:
        print(f"Parsing {pdf.name}...")
        result = converter.convert(str(pdf))
        
        # Exporting natively to structured Markdown
        md_content = result.document.export_to_markdown()
        
        out_path = Path(output_directory) / f"{pdf.stem}.md"
        out_path.write_text(md_content, encoding="utf-8")
        print(f"Saved: {out_path}")

# Run the batch job
batch_convert_manuals("./synopsys_pdfs", "./parsed_markdown")