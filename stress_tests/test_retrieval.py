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

def run_retrieval_stress_test(retriever, test_cases):
    results = []
    
    for test in test_cases:
        instruction = test["instruction"]
        expected = test["expected_command"]
        
        scenarios = {
            "Perfect Retrieval": retriever.retrieve_tcl_context(instruction, top_k=3),
            "Partial Retrieval": retriever.retrieve_partial_context(instruction, k=3),
            "Wrong Retrieval": retriever.retrieve_random_context(k=3),
            "No Retrieval": "No context available."
        }
        
        test_results = {
            "id": test["id"],
            "instruction": instruction,
            "scenarios": {}
        }
        
        for scenario_name, context in scenarios.items():
            prompt = build_rag_prompt(instruction, context)
            t0 = time.perf_counter()
            response = generate_with_ollama(prompt)
            latency = time.perf_counter() - t0
            
            exact_match = 1 if response.strip() == expected else 0
            
            test_results["scenarios"][scenario_name] = {
                "response": response,
                "latency": latency,
                "exact_match": exact_match
            }
            
        results.append(test_results)
        
    return results
