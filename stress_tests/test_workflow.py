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
