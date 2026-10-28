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

def run_hallucination_test(retriever, test_cases):
    results = []
    
    for test in test_cases:
        instruction = test["instruction"]
        expected_refusals = [k.lower() for k in test["expected_refusal_keywords"]]
        
        # In reality, this command shouldn't exist, but we still do normal retrieval
        context = retriever.retrieve_tcl_context(instruction, top_k=3)
        prompt = build_rag_prompt(instruction, context)
        
        t0 = time.perf_counter()
        response = generate_with_ollama(prompt)
        latency = time.perf_counter() - t0
        
        response_lower = response.lower()
        
        # Check if the model refused to answer
        refused = any(k in response_lower for k in expected_refusals)
        hallucinated = not refused
        
        results.append({
            "id": test["id"],
            "instruction": instruction,
            "response": response,
            "latency": latency,
            "hallucinated": 1 if hallucinated else 0,
            "refused": 1 if refused else 0
        })
        
    return results
