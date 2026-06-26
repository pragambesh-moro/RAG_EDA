import os
import json
import time
import requests
from datetime import datetime
from pathlib import Path
from rag_retriever import TclRagRetriever

RESULTS_DIR = "./eval_results"
DATA_FILE = "./test_data/benchmark_50_queries.json"

MODEL_BASE = "deepseek-coder:6.7b-base"
MODEL_SFT = "eda-coder"

def generate_with_ollama(model_name: str, prompt: str) -> tuple[str, float]:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "system": "You are an expert Synopsys EDA physical design assistant. You must output ONLY the precise Tcl command requested based on the provided context. Do not provide explanations, markdown formatting, or preamble.",
        "prompt": prompt,
        "stream": False,
        "keep_alive": 0,
        "options": {
            "temperature": 0.1,
            "top_p": 0.95,
        }
    }
    
    t0 = time.perf_counter()
    try:
        response = requests.post(url, json=payload, timeout=1200)
        response.raise_for_status()
        data = response.json()
        latency = time.perf_counter() - t0
        return data.get("response", "").strip(), latency
    except Exception as e:
        latency = time.perf_counter() - t0
        return f"ERROR: {str(e)}", latency

def build_rag_prompt(instruction: str, context: str) -> str:
    return (
        "Use the following Synopsys manual extracts to formulate your command.\n\n"
        f"---\n{context}\n---\n\n"
        f"Query: {instruction}\n"
    )

def main():
    print("=" * 80)
    print(" MISSING BENCHMARK: Base+RAG vs SFT+RAG (Ablation Study)")
    print("=" * 80)

    if not os.path.exists(DATA_FILE):
        print(f"ERROR: Could not find test data at {DATA_FILE}")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        queries = json.load(f)

    # Check Ollama Status
    try:
        requests.get("http://localhost:11434")
    except requests.exceptions.ConnectionError:
        print("\nERROR: Could not connect to Ollama.")
        return

    print("\nInitializing RAG Retriever...")
    retriever = TclRagRetriever()
    print("Retriever ready.\n")

    results = []
    total_latency_base = 0.0
    total_latency_sft = 0.0

    print(f"Running Benchmark on {len(queries)} queries...\n")
    
    for idx, item in enumerate(queries, 1):
        instruction = item["instruction"]
        category = item["category"]
        
        print(f"\n[{idx:02d}/{len(queries)}] [{category}] {instruction[:60]}...")
        
        print("   -> [1/3] Retrieving ChromaDB context... ", end="", flush=True)
        t_ctx = time.perf_counter()
        context = retriever.retrieve_tcl_context(instruction, top_k=5)
        print(f"done ({time.perf_counter()-t_ctx:.2f}s)")
        
        prompt = build_rag_prompt(instruction, context)
        
        print(f"   -> [2/3] Generating Base Model ({MODEL_BASE})... ", end="", flush=True)
        base_resp, base_time = generate_with_ollama(MODEL_BASE, prompt)
        total_latency_base += base_time
        print(f"done ({base_time:.2f}s)")
        
        print(f"   -> [3/3] Generating SFT Model ({MODEL_SFT})... ", end="", flush=True)
        sft_resp, sft_time = generate_with_ollama(MODEL_SFT, prompt)
        total_latency_sft += sft_time
        print(f"done ({sft_time:.2f}s)")
        
        # Store Result
        results.append({
            "id": idx,
            "category": category,
            "query": instruction,
            "base_model_rag": {
                "output": base_resp,
                "latency_sec": round(base_time, 2)
            },
            "sft_model_rag": {
                "output": sft_resp,
                "latency_sec": round(sft_time, 2)
            }
        })

    # Save Report
    Path(RESULTS_DIR).mkdir(exist_ok=True)
    out_path = Path(RESULTS_DIR) / "missing_benchmark_results.json"
    
    report = {
        "metadata": {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "base_model": MODEL_BASE,
            "sft_model": MODEL_SFT,
            "total_queries": len(queries),
            "avg_latency_base_sec": round(total_latency_base / len(queries), 2),
            "avg_latency_sft_sec": round(total_latency_sft / len(queries), 2)
        },
        "results": results
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 80)
    print(f"Benchmark Complete!")
    print(f"Avg Base Latency: {report['metadata']['avg_latency_base_sec']}s")
    print(f"Avg SFT Latency : {report['metadata']['avg_latency_sft_sec']}s")
    print(f"Results saved to: {out_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()
