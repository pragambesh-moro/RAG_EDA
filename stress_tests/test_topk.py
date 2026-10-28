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
from tcl_inference import build_rag_prompt, generate_with_ollama

def run_topk_ablation_test(retriever, test_cases):
    results = []
    
    for test in test_cases:
        instruction = test["instruction"]
        expected = test["expected_command"]
        
        test_results = {
            "id": test["id"],
            "instruction": instruction,
            "scenarios": {}
        }
        
        for k in [1, 2, 3, 5]:
            print(f"    - Evaluating k={k}...")
            context = retriever.retrieve_tcl_context(instruction, top_k=k)
            prompt = build_rag_prompt(instruction, context)
            
            t0 = time.perf_counter()
            response = generate_with_ollama(prompt)
            latency = time.perf_counter() - t0
            print(f"      -> Done in {latency:.2f}s")
            
            exact_match = 1 if response.strip() == expected else 0
            
            test_results["scenarios"][f"top-{k}"] = {
                "response": response,
                "latency": latency,
                "exact_match": exact_match
            }
            
        results.append(test_results)
        
    return results
