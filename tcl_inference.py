"""
tcl_inference.py — The Final RAG + SFT Application

This script combines Phase 3 (Vector Retrieval) with Phase 4 (SFT Generation).
It takes a plain-English physical design query, searches the Synopsys 
manuals in ChromaDB for context, and asks the locally-trained QLoRA model
to generate the exact Tcl command.

Usage:
    python tcl_inference.py
"""

import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel
from rag_retriever import TclRagRetriever

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
MODEL_ID = "./deepseek-coder-7b-base"
ADAPTER_PATH = "./qlora-tcl-model-local"

def load_inference_model():
    print(f"Loading 4-bit Base Model from {MODEL_ID}...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID, quantization_config=bnb_config, device_map="auto"
    )
    
    print(f"Applying LoRA Adapters from {ADAPTER_PATH}...")
    model = PeftModel.from_pretrained(model, ADAPTER_PATH)
    model.eval()
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token
    return model, tokenizer

def build_rag_prompt(instruction: str, context: str) -> str:
    """
    Injects the retrieved manual chunks directly into the prompt so the model
    doesn't have to rely purely on zero-shot memory.
    """
    return (
        "### Context:\n"
        "Use the following Synopsys manual extracts to formulate your command.\n"
        f"{context}\n\n"
        f"### Instruction:\n{instruction}\n\n"
        "### Response:\n"
    )

def main():
    # Prevent Windows trl/pathlib encoding crashes
    os.environ["PYTHONUTF8"] = "1"
    
    print("=" * 60)
    print("EDA Tool Command LLM — Interactive Shell")
    print("=" * 60)
    
    # 1. Spin up the Vector DB
    retriever = TclRagRetriever()
    
    # 2. Spin up the Fine-Tuned Model
    model, tokenizer = load_inference_model()
    
    print("\nSystem ready! Type 'quit' to exit.")
    
    while True:
        print("\n" + "─"*60)
        user_intent = input("Enter physical design intent:\n> ")
        if user_intent.strip().lower() in ['quit', 'exit', 'q']:
            break
            
        print("\n[1/2] Retrieving Synopsys Manual Context...")
        context = retriever.retrieve_tcl_context(user_intent, top_k=2)
        
        prompt = build_rag_prompt(user_intent, context)
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        print("[2/2] Generating Tcl Command...")
        with torch.inference_mode():
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=False,
                repetition_penalty=1.0,     # MUST be 1.0 to preserve spaces in code
                eos_token_id=tokenizer.eos_token_id,
            )
            
        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
        response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
        
        print("\n>>> GENERATED COMMAND:")
        # Print green text for visibility if terminal supports it
        print(f"\033[92m{response}\033[0m")

if __name__ == "__main__":
    main()
