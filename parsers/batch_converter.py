################################################################################
# Copyright (c) 2026, Shiv Nadar University, Delhi NCR, India. All Rights
# Reserved. Permission to use, copy, modify and distribute this software for
# educational, research, and not-for-profit purposes, without fee and without a
# signed license agreement, is hereby granted, provided that this paragraph and
# the following two paragraphs appear in all copies, modifications, and
# distributions.
#
# IN NO EVENT SHALL SHIV NADAR UNIVERSITY BE LIABLE TO ANY PARTY FOR DIRECT,
# INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST
# PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE.
#
# SHIV NADAR UNIVERSITY SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS PROVIDED "AS IS". SHIV
# NADAR UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
# ENHANCEMENTS, OR MODIFICATIONS.
#
# Revision History:
# Date          By                     Change Notes
# ------------ ---------------------- ------------------------------------------ 
#               Pragambesh Moro        Initial commit
################################################################################

import os
import gc
import argparse
from pathlib import Path
import pypdfium2 as pdfium

# Try to import torch to clear CUDA cache between chunks
try:
    import torch
    has_torch = True
except ImportError:
    has_torch = False

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.pipeline_options import AcceleratorOptions, AcceleratorDevice

def get_pdf_page_count(pdf_path: str) -> int:
    try:
        pdf_doc = pdfium.PdfDocument(pdf_path)
        count = len(pdf_doc)
        pdf_doc.close()
        return count
    except Exception as e:
        print(f"Warning: Could not read page count for {pdf_path}: {e}")
        return 99999 # Fallback

def batch_convert_manuals(pdf_directory: str, output_directory: str, num_threads: int, ocr_batch_size: int, layout_batch_size: int, use_gpu: bool, chunk_size: int):
    # Configure GPU/CPU Device
    device = AcceleratorDevice.CUDA if use_gpu else AcceleratorDevice.CPU
    accelerator_options = AcceleratorOptions(num_threads=num_threads, device=device)
    
    # Configure Pipeline for optimization based on machine constraints
    pipeline_options = PdfPipelineOptions(accelerator_options=accelerator_options)
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
        out_path = Path(output_directory) / f"{pdf.stem}.md"
        if out_path.exists():
            print(f"Skipping {pdf.name}... (Markdown already exists)")
            continue

        print(f"Parsing {pdf.name}...")
        total_pages = get_pdf_page_count(str(pdf))
        print(f"Total pages detected: {total_pages}")
        
        full_md_content = []
        
        # Process in chunks to prevent memory accumulation leak
        for start_page in range(1, total_pages + 1, chunk_size):
            end_page = min(start_page + chunk_size - 1, total_pages)
            print(f"  -> Processing pages {start_page} to {end_page}...")
            
            try:
                # Isolate the conversion to a specific range of pages
                result = converter.convert(str(pdf), page_range=(start_page, end_page))
                full_md_content.append(result.document.export_to_markdown())
            except Exception as e:
                print(f"  -> Error processing chunk {start_page}-{end_page}: {e}")
                
            # FORCE MEMORY CLEARING: This is critical for preventing OOM on massive documents
            if has_torch and use_gpu:
                torch.cuda.empty_cache()
            gc.collect()
            
        # Write combined markdown chunks to a single file
        if full_md_content:
            out_path = Path(output_directory) / f"{pdf.stem}.md"
            out_path.write_text("\n\n".join(full_md_content), encoding="utf-8")
            print(f"Saved: {out_path}\n")
        else:
            print(f"Failed to extract any content from {pdf.name}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch convert EDA PDFs to Markdown with Docling.")
    parser.add_argument("--pdf_dir", type=str, default="./synopsys_pdfs", help="Directory containing raw PDFs")
    parser.add_argument("--out_dir", type=str, default="./parsed_markdown", help="Output directory for Markdown files")
    parser.add_argument("--num_threads", type=int, default=4, help="Number of CPU threads")
    parser.add_argument("--ocr_batch_size", type=int, default=2, help="OCR batch size")
    parser.add_argument("--layout_batch_size", type=int, default=2, help="Layout batch size")
    parser.add_argument("--use_gpu", action="store_true", help="Enable CUDA GPU acceleration")
    parser.add_argument("--chunk_size", type=int, default=50, help="Pages to process per chunk to prevent OOM")
    
    args = parser.parse_args()
    
    print(f"Starting conversion: Threads={args.num_threads} | OCR Batch={args.ocr_batch_size} | Layout Batch={args.layout_batch_size} | GPU={args.use_gpu} | Chunk={args.chunk_size}")
    batch_convert_manuals(
        args.pdf_dir, 
        args.out_dir, 
        args.num_threads, 
        args.ocr_batch_size, 
        args.layout_batch_size,
        args.use_gpu,
        args.chunk_size
    )