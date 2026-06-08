# EDA Tool Command LLM

> A hybrid RAG + QLoRA pipeline that ingests Synopsys EDA tool manuals and translates plain-English physical design intent into syntactically correct Tcl commands.

## Overview

Physical design engineers working with Synopsys tools like IC Compiler II and Design Compiler spend significant time looking up the correct Tcl command syntax across thousands of pages of documentation. This project automates that process end-to-end.

The system works in two complementary stages:

1. **RAG (Primary)** — At inference time, a plain-English query is embedded and matched against a locally-hosted Vector Database of 23,000+ indexed manual chunks. The most relevant documentation context is retrieved and fed to a Code LLM, grounding its output in the actual manual.

2. **QLoRA SFT (Fallback)** — A `deepseek-coder-7b-base` model is fine-tuned on a synthetic instruction dataset extracted from the same manuals, teaching the model Synopsys-specific command idioms that general-purpose LLMs are unaware of.

---

## Architecture

```
Raw PDFs (Synopsys Manuals)
        │
        ▼
┌─────────────────────┐
│  batch_converter.py │  ← Layout-aware PDF parsing (docling)
│  Phase 1: Ingestion │    Page-range batching to avoid OOM
└────────┬────────────┘
         │  parsed_markdown/
         ▼
┌──────────────────────┐
│ semantic_chunker.py  │  ← Header-level Markdown splitting
│ Phase 2: Chunking    │    Preserves Tcl blocks intact
└────────┬─────────────┘
         │  semantic_chunks.jsonl  (~23,000 chunks)
         ▼
┌──────────────────────┐       ┌─────────────────────────┐
│  build_vector_db.py  │       │  generate_sft_dataset.py│
│  Phase 3: Embedding  │       │  Phase 4: SFT Data Gen  │
│  bge-small-en-v1.5   │       │  Heuristic Tcl extractor│
│  ChromaDB (local)    │       └────────────┬────────────┘
└────────┬─────────────┘                    │  dataset.jsonl
         │  chroma_db/                      ▼
         ▼                       ┌──────────────────────┐
┌──────────────────────┐         │   qlora_train.py     │
│  rag_retriever.py    │         │   HPC: A100 (20GB)   │
│  Cosine Similarity   │         │   4-bit QLoRA / PEFT │
│  BGE prefix encoding │         │   hpc_submit.slurm   │
└──────────────────────┘         └──────────────────────┘
```

---

## Repository Structure

```
RAG_EDA/
├── batch_converter.py        # Phase 1: PDF → Markdown via docling
├── semantic_chunker.py       # Phase 2: Markdown → semantic_chunks.jsonl
├── build_vector_db.py        # Phase 3: Chunks → ChromaDB embeddings
├── rag_retriever.py          # Phase 3: Query → Top-K context retrieval
├── generate_sft_dataset.py   # Phase 4: Chunks → dataset.jsonl (local)
├── qlora_train.py            # Phase 4: QLoRA fine-tuning (HPC)
├── hpc_submit.slurm          # Phase 4: Slurm batch submission script
├── download_hf_model.py      # Helper: Download model weights locally
├── download_hpc_wheels.py    # Helper: Download Linux wheels for HPC transfer
├── hpc.md                    # HPC cluster reference notes
├── parsed_markdown/          # Output: Raw markdown from PDFs
├── semantic_chunks.jsonl     # Output: 23,000+ indexed chunks
├── chroma_db/                # Output: Persistent local vector store
└── dataset.jsonl             # Output: SFT instruction-output pairs
```

---

## Quick Start

### Prerequisites
- Python 3.11+
- CUDA-enabled GPU (optional for Phase 3, required for Phase 4)
- Synopsys PDF manuals placed in `./synopsys_pdfs/`

### Installation
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install docling langchain-text-splitters langchain-huggingface langchain-chroma chromadb sentence-transformers
```

### Phase 1–3: Local RAG Pipeline
```bash
# Convert PDFs to structured Markdown
python batch_converter.py --pdf_dir ./synopsys_pdfs --out_dir ./parsed_markdown --num_threads 4

# Chunk Markdown at semantic header boundaries
python semantic_chunker.py

# Build the local vector database (~28 min on CPU)
python build_vector_db.py

# Test a retrieval query
python rag_retriever.py
```

### Phase 4: HPC Fine-Tuning (Offline)
```bash
# 1. Generate synthetic instruction dataset locally
python generate_sft_dataset.py

# 2. Download Linux-compatible wheels and model weights locally
python download_hpc_wheels.py
python download_hf_model.py

# 3. Transfer to HPC via scp/rsync, then on the login node:
pip install --no-index --find-links ./hpc_wheels transformers peft trl bitsandbytes datasets accelerate

# 4. Submit the training job
sbatch hpc_submit.slurm
```

---

## Key Design Decisions

| Decision | Rationale |
|---|---|
| `docling` for PDF parsing | Preserves table structures and code blocks that standard PDF text extractors destroy |
| Page-range batching (50 pages) | Prevents `std::bad_alloc` OOM crashes on machines with ≤ 32GB RAM |
| Header-level chunking | Guarantees Tcl command blocks are never split across embedding boundaries |
| `bge-small-en-v1.5` embeddings | Asymmetric retrieval model optimized for short query → long document matching |
| BGE instruction prefix | Required by the model architecture to activate asymmetric retrieval mode |
| ChromaDB (local) | Zero-latency, no network dependency, persistent across sessions |
| `deepseek-coder-7b-base` | Code-specialized pre-training; base model avoids instruct bias for custom SFT |
| QLoRA 4-bit (`nf4` + double quant) | Reduces a 7B model to ~6GB VRAM; fits in a 20GB MIG GPU allocation |
| Offline HPC wheel transfer | HPC compute/login nodes have no outbound internet access |

---

## Hardware Reference

| Stage | Machine | Key Specs |
|---|---|---|
| Phase 1–2 (Ingestion) | Local | Intel Core i9-13900HX, 32GB RAM |
| Phase 3 (Embedding) | Local | i9-13900HX, CPU-only, ~28 min |
| Phase 4 (Training) | HPC | 2× A100 MIG 10GB slices, 256GB RAM |

---

## License

For internal research use only. Synopsys documentation is proprietary.
