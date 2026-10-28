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
