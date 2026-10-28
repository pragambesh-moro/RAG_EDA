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

def run_workflow_test(retriever, test_cases):
    results = []
    
    for test in test_cases:
        instruction = test["instruction"]
        expected_commands = test["expected_commands"]
        
        # Increase top_k slightly for complex workflows to gather more context
        context = retriever.retrieve_tcl_context(instruction, top_k=5)
        prompt = build_rag_prompt(instruction, context)
        
        t0 = time.perf_counter()
        response = generate_with_ollama(prompt)
        latency = time.perf_counter() - t0
        
        # Calculate how many of the expected commands are present in the output
        found_commands = []
        missing_commands = []
        for cmd in expected_commands:
            if cmd in response:
                found_commands.append(cmd)
            else:
                missing_commands.append(cmd)
                
        workflow_success_rate = len(found_commands) / len(expected_commands) if expected_commands else 0
        exact_match = 1 if workflow_success_rate == 1.0 else 0
        
        results.append({
            "id": test["id"],
            "instruction": instruction,
            "response": response,
            "latency": latency,
            "workflow_success_rate": workflow_success_rate,
            "exact_match": exact_match,
            "missing_commands": missing_commands
        })
        
    return results
