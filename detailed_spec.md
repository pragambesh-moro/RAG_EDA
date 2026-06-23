# EDA Coder: Detailed Technical Specification

## 1. System Objective
The goal of this project is to build an autonomous agent that translates plain-English instructions (e.g., "Create a floorplan with a core utilization of 0.7") into syntactically valid Synopsys Tcl commands (e.g., `initialize_floorplan -core_utilization 0.7`). 

General LLMs fail at this because the manuals for IC Compiler II, Design Compiler, and PrimeTime are strictly proprietary and omitted from their training datasets. We solve this by combining **Supervised Fine-Tuning (SFT)** with **Retrieval-Augmented Generation (RAG)**.

---

## 2. Ingestion & Preprocessing (Phases 1 & 2)

### 2.1 PDF Extraction (`batch_converter.py`)
Traditional PDF parsers (`pypdf2`, `pdfminer`) extract text linearly, which destroys the complex tabular data and multi-column code blocks found in Synopsys manuals. 
- **Tool**: We use `docling` with layout-aware document analysis.
- **Optimization**: Parsing 2,000-page proprietary PDFs causes massive memory spikes. We implemented a batched-processing algorithm that segments PDFs into 50-page chunks, converts them to Markdown iteratively, and aggressively frees memory (`del` + `gc.collect()`), allowing parsing on a 32GB RAM local machine without `std::bad_alloc` crashes.

### 2.2 Semantic Chunking (`semantic_chunker.py`)
Standard LangChain recursive token splitters often slice physical code blocks in half, destroying the Tcl syntax. 
- **Tool**: `MarkdownHeaderTextSplitter`.
- **Strategy**: We split the parsed markdown purely on structural headers (`#`, `##`, `###`). This guarantees that command descriptions and their associated code blocks remain contiguous within the same chunk.
- **Output**: `semantic_chunks.jsonl` containing ~23,000 distinct, self-contained documentation blocks.

---

## 3. RAG Pipeline (Phase 3)

### 3.1 Vector Embedding (`build_vector_db.py`)
- **Embedding Model**: `BAAI/bge-small-en-v1.5`. Chosen specifically for its asymmetric retrieval capabilities (mapping a short, natural language user query to a massive block of dense technical text).
- **Format Requirement**: User queries must be prepended with `Represent this sentence for searching relevant passages: ` to trigger the model's asymmetric mode.
- **Storage**: `ChromaDB` running entirely locally via SQLite. This ensures zero network latency and no exposure of proprietary documentation to external APIs.

### 3.2 Context Retrieval (`rag_retriever.py`)
At inference time, the user's plain-English query undergoes Cosine Similarity matching against the Vector Database. The top 3 most relevant manual chunks are extracted and formatted into a strict system prompt context window.

---

## 4. Supervised Fine-Tuning (Phase 4)

### 4.1 Synthetic Dataset Generation (`generate_sft_dataset.py`)
To teach the model Synopsys Tcl idioms, we generated an instruction-tuning dataset from the manuals.
- **Extraction Logic**: We use regular expressions to identify chunks containing inline code blocks with common EDA keywords (`icc2_shell>`, `set_app_options`, `create_placement`). 
- **Formatting**: The extracted blocks are reformatted into Alpaca-style `{instruction, output}` pairs, stored in `dataset.jsonl`.

### 4.2 QLoRA Local AMD Training (`qlora_train_local.py`)
We fine-tuned the `deepseek-coder-7b-base` model locally.
- **Hardware**: Local Windows machine utilizing WSL (Windows Subsystem for Linux) and an AMD GPU.
- **Environment**: Configured using AMD ROCm (`HSA_OVERRIDE_GFX_VERSION`) to enable native PyTorch acceleration on consumer AMD silicon, bypassing the need for an enterprise HPC cluster.
- **Quantization**: 4-bit `nf4` NormalFloat quantization with double quantization enabled. This allowed us to train a 7B parameter model within a highly restricted consumer VRAM footprint.
- **LoRA Config**: `r=16`, `alpha=32`, targeting `q_proj`, `v_proj`, `k_proj`, and `o_proj`.

---

## 5. Merging, Quantization, and Deployment

### 5.1 Merging and GGUF Conversion
The raw LoRA adapter weights (`adapter_model.safetensors`) were merged back into the base FP16 model using `peft.merge_and_unload()`. During this step, the embedding tensors had to be manually resized via `base_model.resize_token_embeddings(len(tokenizer))` to resolve a mismatch with the specialized BPE tokenizer.
The merged model was then converted to `GGUF` format via `llama.cpp` and quantized to `Q4_K_M` to reduce the file size from 14GB to 4GB.

### 5.2 Ollama Integration (`Modelfile` & `tcl_inference.py`)
Instead of running heavy PyTorch `transformers` pipelines at inference time, the model is injected into a local `ollama` registry.
- **Performance**: Inference is accelerated by `llama.cpp`'s highly optimized CPU/GPU backend, dropping generation latency from minutes to ~10-15 seconds per RAG query.
- **System Prompt**: A strict system prompt forces the model to synthesize the RAG context and output **only** valid Tcl commands, suppressing conversational conversational filler.

---

## 6. End-to-End Execution Flow

1. User types query in terminal via `tcl_inference.py`.
2. `TclRagRetriever` encodes the query using `bge-small-en`.
3. `ChromaDB` returns the top 3 Synopsys manual chunks.
4. The chunks are injected into the Ollama payload alongside the query and strict system prompt.
5. The local `eda-coder` GGUF processes the augmented prompt.
6. The terminal outputs the syntactically correct Tcl script.
