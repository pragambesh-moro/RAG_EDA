import time
import json
from evaluate_model import TEST_QUERIES, run_inference
from rag_retriever import TclRagRetriever
from tcl_inference import build_rag_prompt, generate_with_ollama

def main():
    print("=" * 80)
    print("STRESS TEST: Base Model (SFT) vs. RAG Pipeline")
    print("=" * 80)
    
    print("\nInitializing RAG Retriever...")
    retriever = TclRagRetriever()
    print("Retriever ready.\n")
    
    results = []
    
    for idx, query in enumerate(TEST_QUERIES[:4], 1):
        instruction = query["instruction"]
        category = query["category"]
        print(f"\n[{idx:02d}/4] [{category}]", flush=True)
        print(f"Q: {instruction}", flush=True)
        
        # 1. Base Model (No RAG)
        # Using evaluate_model's run_inference which includes the strict system prompt
        base_ans, base_lat = run_inference("eda-coder", instruction)
        
        # 2. RAG Pipeline
        t0 = time.perf_counter()
        context = retriever.retrieve_tcl_context(instruction, top_k=2)
        rag_prompt = build_rag_prompt(instruction, context)
        rag_ans = generate_with_ollama(rag_prompt)
        rag_lat = time.perf_counter() - t0
        
        print(f"   [Base SFT ] ({base_lat:.2f}s): {base_ans}")
        print(f"   [SFT + RAG] ({rag_lat:.2f}s): {rag_ans}")
        
        results.append({
            "category": category,
            "instruction": instruction,
            "base_answer": base_ans,
            "base_latency": round(base_lat, 2),
            "rag_answer": rag_ans,
            "rag_latency": round(rag_lat, 2)
        })
        
    with open("rag_vs_base_comparison.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print("\n" + "=" * 80)
    print("Stress test complete! Results saved to rag_vs_base_comparison.json")

if __name__ == "__main__":
    main()
