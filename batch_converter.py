import os
import argparse
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.pipeline_options import AcceleratorOptions, AcceleratorDevice

def batch_convert_manuals(pdf_directory: str, output_directory: str, num_threads: int, ocr_batch_size: int, layout_batch_size: int, use_gpu: bool):
    # Configure GPU/CPU Device
    device = AcceleratorDevice.CUDA if use_gpu else AcceleratorDevice.CPU
    accelerator_options = AcceleratorOptions(num_threads=num_threads, device=device)
    
    # Configure Pipeline for optimization based on machine constraints
    pipeline_options = PdfPipelineOptions(accelerator_options=accelerator_options)
    # Some older versions of docling might use num_threads directly on pipeline_options, 
    # but accelerator_options is the modern way. We'll set it on pipeline_options as well just in case.
    if hasattr(pipeline_options, 'num_threads'):
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
    parser.add_argument("--num_threads", type=int, default=2, help="Number of CPU threads")
    parser.add_argument("--ocr_batch_size", type=int, default=1, help="OCR batch size")
    parser.add_argument("--layout_batch_size", type=int, default=1, help="Layout batch size")
    parser.add_argument("--use_gpu", action="store_true", help="Enable CUDA GPU acceleration")
    
    args = parser.parse_args()
    
    print(f"Starting conversion: Threads={args.num_threads} | OCR Batch={args.ocr_batch_size} | Layout Batch={args.layout_batch_size} | GPU={args.use_gpu}")
    batch_convert_manuals(
        args.pdf_dir, 
        args.out_dir, 
        args.num_threads, 
        args.ocr_batch_size, 
        args.layout_batch_size,
        args.use_gpu
    )