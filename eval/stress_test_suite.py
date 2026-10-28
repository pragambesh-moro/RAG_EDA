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
import json
import time
import requests
from datetime import datetime
from pathlib import Path

from rag_retriever import TclRagRetriever

from stress_tests.test_retrieval import run_retrieval_stress_test
from stress_tests.test_hallucination import run_hallucination_test
from stress_tests.test_topk import run_topk_ablation_test
from stress_tests.test_prompt_wording import run_prompt_wording_test
from stress_tests.test_workflow import run_workflow_test

RESULTS_DIR = "./eval_results"
DATA_FILE = "./test_data/stress_test_data.json"

def main():
    print("=" * 70)
    print("EDA TCL RAG + LoRA Assistant - Comprehensive Stress Test Suite")
    print("=" * 70)

    # 1. Load Test Data
    if not os.path.exists(DATA_FILE):
        print(f"ERROR: Could not find test data at {DATA_FILE}")
        return
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        test_data = json.load(f)
        
    # 2. Check Ollama Status
    try:
        requests.get("http://localhost:11434")
    except requests.exceptions.ConnectionError:
        print("\nERROR: Could not connect to Ollama. Ensure the daemon is running.")
        return

    # 3. Initialize Retriever
    print("\nInitializing RAG Retriever...")
    retriever = TclRagRetriever()
    print("Retriever ready.\n")

    report = {
        "metadata": {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "model_name": "eda-coder"
        },
        "tests": {}
    }

    t_start = time.perf_counter()

    # --- Test 1: Retrieval Stress Test ---
    print("Running Test 1: Retrieval Stress Test...")
    retrieval_results = run_retrieval_stress_test(retriever, test_data.get("retrieval_tests", []))
    report["tests"]["retrieval_stress_test"] = retrieval_results

    # --- Test 2: Hallucination Test ---
    print("Running Test 2: Out-of-Manual Hallucination Test...")
    hallucination_results = run_hallucination_test(retriever, test_data.get("hallucination_tests", []))
    report["tests"]["hallucination_test"] = hallucination_results

    # --- Test 3: Top-K Ablation Test ---
    print("Running Test 3: Top-K Retrieval Ablation...")
    topk_results = run_topk_ablation_test(retriever, test_data.get("topk_tests", []))
    report["tests"]["topk_ablation"] = topk_results

    # --- Test 4: Prompt Wording Test ---
    print("Running Test 4: Prompt Wording Robustness Test...")
    wording_results = run_prompt_wording_test(retriever, test_data.get("prompt_wording_tests", []))
    report["tests"]["prompt_wording"] = wording_results

    # --- Test 5: End-to-End Workflow Test ---
    print("Running Test 5: End-to-End Workflow Evaluation...")
    workflow_results = run_workflow_test(retriever, test_data.get("workflow_tests", []))
    report["tests"]["workflow_evaluation"] = workflow_results

    total_time = time.perf_counter() - t_start
    report["metadata"]["total_execution_time_seconds"] = round(total_time, 2)

    # 4. Save Report
    Path(RESULTS_DIR).mkdir(exist_ok=True)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = Path(RESULTS_DIR) / f"stress_test_report_{timestamp_str}.json"
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 70)
    print(f"Stress test suite completed in {total_time:.2f}s!")
    print(f"Results saved to: {out_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
