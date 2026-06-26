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
