"""
tcl_inference.py — The Final RAG + SFT Application via Ollama

This script takes a plain-English physical design query, searches the Synopsys 
manuals in ChromaDB for context, and asks the local Ollama model to generate 
the exact Tcl command.

Usage:
    python tcl_inference.py
"""

import os
import requests
import json
from rag_retriever import TclRagRetriever

MODEL_NAME = "eda-coder"

def print_banner():
    C = "\033[96m" # Cyan
    G = "\033[92m" # Green
    R = "\033[0m"  # Reset
    banner = f"""{C}
███████╗██████╗  █████╗       ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗     ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
█████╗  ██║  ██║███████║     ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║  ██║██╔══██║     ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
███████╗██████╔╝██║  ██║     ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚══════╝╚═════╝ ╚═╝  ╚═╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
{G}           v1.0.0 - Air-Gapped Tcl Generation Pipeline{R}
"""
    print(banner)

def generate_with_ollama(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": MODEL_NAME,
        "system": "You are an expert Synopsys EDA physical design assistant. You must output ONLY the precise Tcl command requested based on the provided context. If the requested command, tool, or flag is NOT explicitly supported or found in the provided manual context, you MUST refuse by stating: 'I cannot find this in the manual.' Do not invent or guess commands. Do not provide explanations, markdown formatting, or preamble.",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.95,
            "num_ctx": 8192,
        }
    }
    try:
        response = requests.post(url, json=payload, timeout=180)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.Timeout:
        return "ERROR: Request to Ollama timed out."
    except requests.exceptions.ConnectionError:
        return "ERROR: Could not connect to Ollama. Please ensure Ollama is running."
    except Exception as e:
        return f"ERROR: {str(e)}"

def build_rag_prompt(instruction: str, context: str) -> str:
    """
    Injects the retrieved manual chunks directly into the prompt.
    The Ollama Modelfile handles the '### Instruction:' formatting.
    """
    return (
        "Use the following Synopsys manual extracts to formulate your command.\n\n"
        f"---\n{context}\n---\n\n"
        f"Query: {instruction}\n"
    )

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print("Loading RAG Retriever...")
    print("\n" + "=" * 60)
    print("   EDA Coder: AI Physical Design Assistant")
    print("   Powered by Local RAG + QLoRA SFT")
    print("   © Pragambesh Moro - Shiv Nadar University")
    print("=" * 60 + "\n")
    
    # 1. Spin up the Vector DB
    retriever = TclRagRetriever()
    
    # Check if Ollama is running
    try:
        requests.get("http://localhost:11434")
    except requests.exceptions.ConnectionError:
        print("\nERROR: Could not connect to Ollama.")
        print("Please ensure Ollama is running in the background before starting.")
        return
    
    print(f"\nSystem ready! Connected to Ollama model '{MODEL_NAME}'. Type 'quit' to exit.")
    
    while True:
        print("\n" + "─"*60)
        user_intent = input("Enter physical design intent:\n> ")
        if user_intent.strip().lower() in ['quit', 'exit', 'q']:
            break
            
        print("\n[1/2] Retrieving Synopsys Manual Context...")
        context = retriever.retrieve_tcl_context(user_intent, top_k=5)
        
        prompt = build_rag_prompt(user_intent, context)
        
        print(f"[2/2] Generating Tcl Command via Ollama ({MODEL_NAME})...")
        response = generate_with_ollama(prompt)
        
        print("\n>>> GENERATED COMMAND:")
        # Print green text for visibility if terminal supports it
        print(f"\033[92m{response}\033[0m")

if __name__ == "__main__":
    main()
