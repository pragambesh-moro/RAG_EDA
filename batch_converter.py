import os
import argparse
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

def batch_convert_manuals(pdf_directory: str, output_directory: str, num_threads: int, ocr_batch_size: int, layout_batch_size: int):
    # Configure Pipeline for optimization based on machine constraints
    pipeline_options = PdfPipelineOptions()
    pipeline_options.num_threads = num_threads
    pipeline_options.ocr_batch_size = ocr_batch_size
    pipeline_options.layout_batch_size = layout_batch_size

    # Initialize the layout-aware parser
    converter = DocumentConverter(
        allowed_formats=[InputFormat.PDF],
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch convert EDA PDFs to Markdown with Docling.")
    parser.add_argument("--pdf_dir", type=str, default="./synopsys_pdfs", help="Directory containing raw PDFs")
    parser.add_argument("--out_dir", type=str, default="./parsed_markdown", help="Output directory for Markdown files")
    parser.add_argument("--num_threads", type=int, default=2, help="Number of threads (increase if you have a stronger CPU. e.g., 8)")
    parser.add_argument("--ocr_batch_size", type=int, default=1, help="OCR batch size (increase if you have more RAM/VRAM. e.g., 4)")
    parser.add_argument("--layout_batch_size", type=int, default=1, help="Layout batch size (increase if you have more RAM/VRAM. e.g., 4)")
    
    args = parser.parse_args()
    
    print(f"Starting conversion: Threads={args.num_threads} | OCR Batch={args.ocr_batch_size} | Layout Batch={args.layout_batch_size}")
    batch_convert_manuals(
        args.pdf_dir, 
        args.out_dir, 
        args.num_threads, 
        args.ocr_batch_size, 
        args.layout_batch_size
    )