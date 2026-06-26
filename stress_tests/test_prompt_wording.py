import time
from tcl_inference import build_rag_prompt, generate_with_ollama

def run_prompt_wording_test(retriever, test_cases):
    results = []
    
    for test in test_cases:
        expected = test["expected_command"]
        
        test_results = {
            "id": test["id"],
            "variants_tested": len(test["variants"]),
            "variants_results": []
        }
        
        for variant_text in test["variants"]:
            context = retriever.retrieve_tcl_context(variant_text, top_k=3)
            prompt = build_rag_prompt(variant_text, context)
            
            t0 = time.perf_counter()
            response = generate_with_ollama(prompt)
            latency = time.perf_counter() - t0
            
            exact_match = 1 if response.strip() == expected else 0
            
            test_results["variants_results"].append({
                "instruction": variant_text,
                "response": response,
                "latency": latency,
                "exact_match": exact_match
            })
            
        # Calculate consistency: what percentage matched the expected answer
        matches = sum(v["exact_match"] for v in test_results["variants_results"])
        test_results["consistency_score"] = matches / len(test["variants"])
        
        results.append(test_results)
        
    return results
