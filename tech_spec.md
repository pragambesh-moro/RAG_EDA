# Technical Specification: EDA Tool Command LLM
**Version:** 1.0  
**Status:** Phase 4 Training In Progress  
**Author:** pm944  

---

## 1. Problem Statement

Physical design engineers using Synopsys EDA tools (IC Compiler II, Design Compiler, etc.) must manually navigate thousands of pages of user manuals to identify the correct Tcl command syntax for a given design intent. This is time-consuming and error-prone.

**Goal:** Build a locally-hosted system that accepts a plain-English intent (e.g. *"Create a floorplan with 0.7 core utilization"*) and returns the syntactically correct Synopsys Tcl command — without requiring internet access, external APIs, or cloud infrastructure.

---

## 2. System Architecture

The pipeline is split into four sequential phases, divided between local execution and HPC execution.

### 2.1 Data Flow

```
[Raw PDFs] → Phase 1 → [Markdown] → Phase 2 → [Chunks JSONL]
                                                      │
                              ┌───────────────────────┤
                              │                       │
                              ▼                       ▼
                        Phase 3                  Phase 4
                     [ChromaDB]             [dataset.jsonl]
                          │                       │
                          ▼                       ▼
                    [RAG Retrieval]        [QLoRA Training]
                          │                       │
                          └───────────┬───────────┘
                                      ▼
                               [Tcl Command Output]
```

---

## 3. Phase 1: PDF Ingestion

**Script:** `batch_converter.py`  
**Library:** `docling` (IBM Research)  
**Execution Environment:** Local (Windows, i9-13900HX, 32GB RAM)

### 3.1 Why Docling
Standard PDF text extractors (PyMuPDF, pdfplumber) strip layout entirely, collapsing tables into meaningless sequences of numbers. EDA manuals are dense with argument reference tables (e.g., command flags and their types). `docling` uses neural layout analysis to reconstruct these tables in Markdown format, preserving the semantics required for Tcl argument inference.

### 3.2 OOM Resolution
`docling`'s layout parser loads full PyTorch models into memory. At default settings (16 concurrent threads), processing complex pages caused `std::bad_alloc` crashes at around page 400 of large manuals (750+ pages).

**Fix:** Page-range batching — the converter processes documents in sliding windows of 50 pages. After each window, objects are released from memory before the next window is loaded.

**Key Parameters:**
| Parameter | Value | Reason |
|---|---|---|
| `num_threads` | 4 | Avoids VRAM saturation on 8GB RTX 4070 |
| `ocr_batch_size` | 2 | Keeps OCR model memory-bounded |
| `layout_batch_size` | 2 | Prevents layout model buffer overflow |
| Page window size | 50 | Empirically determined safe limit |

---

## 4. Phase 2: Semantic Chunking

**Script:** `semantic_chunker.py`  
**Library:** `langchain-text-splitters` (`MarkdownHeaderTextSplitter`)  
**Execution Environment:** Local

### 4.1 Chunking Strategy
The extracted Markdown is split at `#` (H1) and `##` (H2) header boundaries. This approach was chosen over fixed-character chunking for one critical reason: Tcl command code blocks frequently span multiple lines and reference argument tables in the same section. A fixed-size chunker would fragment these mid-command, producing embeddings that carry only partial syntactic information.

**Output:** `semantic_chunks.jsonl`
- Total chunks: **23,320**
- Each chunk record includes `content` (Markdown text) and `metadata` (Source filename, H1, H2 headers)

### 4.2 Observed Data Quality Issues
A random sample audit of the chunks identified a small number of Tcl commands preceded by `Tcl_` prefix patterns (e.g., `Tcl_GetString`) that are internal C-API calls, not designer-facing commands. These are harmless to the RAG pipeline but were noted for potential exclusion from the SFT dataset.

---

## 5. Phase 3: Vector Storage & Retrieval

**Scripts:** `build_vector_db.py`, `rag_retriever.py`  
**Embedding Model:** `BAAI/bge-small-en-v1.5` (384 dimensions)  
**Vector Store:** ChromaDB (local persistent directory)  
**Execution Environment:** Local (CPU-only)

### 5.1 Embedding Model Selection
`bge-small-en-v1.5` was selected over larger alternatives (e.g., `bge-large`, `text-embedding-ada-002`) for three reasons:

1. **Asymmetric Retrieval Design:** The model is specifically trained for the short-query-to-long-document retrieval pattern. It outperforms many larger symmetric models on this task.
2. **CPU Performance:** At 384 dimensions with quantized weights, it completed embedding of all 23,320 chunks on a CPU-only environment in approximately 28 minutes.
3. **Zero External Dependency:** The model weights are cached locally by `sentence-transformers`. No internet access is required at inference time.

### 5.2 Critical Implementation Detail: BGE Query Prefix
The `bge-small-en-v1.5` architecture requires a specific instruction prefix appended to queries to activate its asymmetric retrieval mode:

```
"Represent this sentence for searching relevant passages: {user_query}"
```

Without this prefix, the model operates in symmetric mode and reverts to superficial keyword matching. This was discovered during initial testing, where the query *"How do I create a floorplan?"* returned only `## See Also` stub sections instead of the substantive `## Creating an Initial Floorplan` content.

### 5.3 Retrieval Performance
Verified with test query *"How do I create a floorplan with 0.7 core utilization?"*:

| Rank | Retrieved Source | Section |
|---|---|---|
| 1 | `icc2-designplan-X-2025.06-SP1.md` | Creating an Initial Floorplan |
| 2 | `dc-ug-X-2025.06.md` | Scaling a Floorplan to a Hybrid-Row Floorplan |
| 3 | `icc2-designplan-X-2025.06-SP1.md` | Creating a Floorplan |

---

## 6. Phase 4: SFT Dataset Generation & QLoRA Training

### 6.1 Dataset Generation

**Script:** `generate_sft_dataset.py`  
**Execution Environment:** Local (no internet dependency)

Since the HPC cluster has no outbound internet access, all dataset generation is performed locally. A heuristic regex-based extractor identifies Markdown code blocks containing valid Tcl syntax (characterized by flag patterns `-[a-z_]+` and snake_case command names). The enclosing section header is reverse-engineered into a plain-English instruction.

**Output format:**
```json
{"instruction": "write the tcl command for creating an initial floorplan.", "output": "initialize_floorplan -core_offset 100"}
```

### 6.2 Base Model Selection

**Model:** `deepseek-ai/deepseek-coder-7b-base`

| Criterion | Justification |
|---|---|
| Code-specialized pre-training | Trained on a multi-language code corpus, giving it strong prior knowledge of command-line syntax patterns |
| Base (not Instruct) variant | Avoids overriding with conversational fine-tuning biases; gives our SFT full control over output format |
| 7B parameter scale | Quantized to 4-bit (`nf4`), the model loads in ~6GB VRAM, fitting comfortably within a 20GB MIG GPU allocation |
| Local hosting capability | Weights can be fully transferred offline and loaded from a local directory with no hub dependency |

### 6.3 QLoRA Training Configuration

**Script:** `qlora_train.py`  
**Library Stack:** `transformers`, `peft`, `trl`, `bitsandbytes`

| Hyperparameter | Value | Rationale |
|---|---|---|
| Quantization | 4-bit `nf4` | NormalFloat4 is optimal for normally-distributed neural network weights |
| Double quantization | Enabled | Saves additional ~0.4 bits/param, further reducing VRAM overhead |
| LoRA rank (`r`) | 16 | Balances adapter expressiveness against parameter efficiency |
| LoRA alpha | 32 | Scaling factor; set to 2× rank as standard practice |
| LoRA target modules | `q_proj`, `v_proj` | Attention projection layers carry the most task-specific knowledge |
| LoRA dropout | 0.05 | Light regularization to prevent adapter overfitting |
| Optimizer | `paged_adamw_8bit` | Offloads optimizer states to CPU RAM when GPU VRAM is pressured |
| Batch size | 4 | Fits within 20GB VRAM with 512-token sequences |
| Gradient accumulation | 4 | Effective batch of 16 for stable gradient estimates |
| Max sequence length | 512 | Covers the longest Tcl command blocks in the dataset |
| Max steps | 500 | Initial training run for evaluation |

### 6.4 Known Bugs Fixed (pre-deployment)

Three critical bugs were identified and corrected before HPC submission:

1. **Double LoRA application:** `get_peft_model()` was called manually *and* `peft_config` was passed to `SFTTrainer`, causing LoRA adapters to be applied twice. Fixed by removing the manual call and delegating entirely to `SFTTrainer`.

2. **Incorrect `formatting_func` signature:** `SFTTrainer` passes examples as *batches* (dict of lists), not individual dicts. The lambda incorrectly treated the entire batch dict as a single example. Fixed by zipping the instruction/output lists within the batch.

3. **Conflicting `dataset_text_field`:** `dataset_text_field="text"` was set despite the dataset having no `"text"` column, causing a silent key error when used alongside `formatting_func`. Removed.

---

## 7. HPC Deployment

**Cluster:** University HPC (Slurm scheduler)  
**Script:** `hpc_submit.slurm`

### 7.1 Hardware Configuration
| Resource | Specification |
|---|---|
| GPU | 2× A100 MIG 10GB slices (`nvidia_a100_80gb_pcie_1g.10gb`) |
| CPUs | 4 (satisfies `QOSMinCpuNotSatisfied` cluster policy) |
| System RAM | 256 GB (auto-allocated by `MinMemoryCPU=64G` × 4 CPUs) |
| Max walltime | 24 hours |
| Partition | `gpu` |

**Note on MIG slice selection:** Two 10GB slices (20GB total VRAM) were chosen over the single full 80GB A100 to dramatically reduce queue time. The cluster has 21 available MIG slices versus 1 full GPU, significantly improving scheduling priority.

### 7.2 Offline Dependency Resolution
The HPC login and compute nodes have no outbound internet access. The following offline transfer workflow was established:

1. Python dependencies downloaded locally as Linux `manylinux2014_x86_64` wheels using `download_hpc_wheels.py`.
2. PyTorch (`torch-2.1.2+cu121`) downloaded directly from `download.pytorch.org` to bypass `pip`'s broken cross-platform solver for custom CUDA indices.
3. `triton==2.1.0` included explicitly to satisfy PyTorch's internal dependency check during offline installation.
4. All wheels and model weights transferred via `rsync`/`scp`.
5. Installed on the HPC using `pip install --no-index --find-links ./hpc_wheels`.

### 7.3 Loaded Modules
```bash
module load cuda/12.8
module load python/3.11.11-cuda
```

---

## 8. Post-Training Steps (Planned)

1. **Download adapters locally:** `scp` the `qlora-tcl-model/` directory (LoRA adapters only, ~200MB) from HPC scratch back to the local machine.
2. **Merge adapters:** Use `peft`'s `merge_and_unload()` to fuse the adapter weights into the base model for single-file inference.
3. **Build inference pipeline:** Combine `rag_retriever.py` (context retrieval) with the merged model (command generation) into a unified `tcl_inference.py` module.
4. **Evaluate:** Benchmark generated commands against a held-out set of known-good Tcl scripts from real design flows.
