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
