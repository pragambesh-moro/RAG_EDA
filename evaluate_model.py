"""
evaluate_model.py — Inference & Evaluation for the QLoRA Fine-Tuned TCL Model

Tests the locally trained LoRA adapters against a curated set of EDA queries,
records outputs, latency, and saves a timestamped JSON results file.

Usage:
    python evaluate_model.py
    python evaluate_model.py --base_model ./deepseek-coder-7b-base --adapters ./qlora-tcl-model-local
"""

import json
import time
import argparse
from datetime import datetime
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# ─────────────────────────────────────────────
# Defaults
# ─────────────────────────────────────────────
DEFAULT_BASE_MODEL = "./deepseek-coder-7b-base"
DEFAULT_ADAPTERS   = "./qlora-tcl-model-local"
RESULTS_DIR        = "./eval_results"

# ─────────────────────────────────────────────
# Test Suite
# Covers all major physical design workflow stages
# ─────────────────────────────────────────────
TEST_QUERIES = [
    # Floorplan
    {
        "category": "Floorplan",
        "instruction": "Create a floorplan with a core utilization of 0.7 and a core offset of 10 microns on all sides.",
    },
    {
        "category": "Floorplan",
        "instruction": "How do I set the aspect ratio of the die to 0.8 during floorplanning?",
    },

    # Placement
    {
        "category": "Placement",
        "instruction": "Run coarse placement while ignoring scan chains.",
    },
    {
        "category": "Placement",
        "instruction": "Place all macros first before placing standard cells.",
    },
    {
        "category": "Placement",
        "instruction": "Fix the placement of a specific cell named 'u_mem_ctrl' so it doesn't move during optimization.",
    },

    # Clock Tree Synthesis
    {
        "category": "CTS",
        "instruction": "Run clock tree synthesis and target a maximum clock skew of 100 picoseconds.",
    },
    {
        "category": "CTS",
        "instruction": "Exclude the clock net named 'clk_scan' from clock tree synthesis.",
    },

    # Routing
    {
        "category": "Routing",
        "instruction": "Run global routing and set the maximum number of routing layers to 9.",
    },
    {
        "category": "Routing",
        "instruction": "Run detail routing and then check for DRC violations.",
    },

    # Timing
    {
        "category": "Timing",
        "instruction": "Report the worst negative slack and the total negative slack across all paths.",
    },
    {
        "category": "Timing",
        "instruction": "Create a clock constraint with a period of 2 nanoseconds on the port named 'clk'.",
    },
    {
        "category": "Timing",
        "instruction": "Set a false path between two registers 'reg_a' and 'reg_b'.",
    },

    # Power
    {
        "category": "Power",
        "instruction": "Report the total power consumption of the design broken down by dynamic and leakage power.",
    },
    {
        "category": "Power",
        "instruction": "Insert power switches for the power domain named 'PD_CPU'.",
    },

    # Design Checks
    {
        "category": "Design Checks",
        "instruction": "Check the design for any unconnected ports or nets.",
    },
    {
        "category": "Design Checks",
        "instruction": "Save the current design state to a file called 'after_route.dcp'.",
    },
]


def build_prompt(instruction: str) -> str:
    return f"### Instruction:\n{instruction}\n\n### Response:\n"


def load_model(base_model_path: str, adapter_path: str):
    print(f"\nLoading base model from: {base_model_path}")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        quantization_config=bnb_config,
        device_map="auto",
    )

    print(f"Loading LoRA adapters from: {adapter_path}")
    model = PeftModel.from_pretrained(model, adapter_path)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    tokenizer.pad_token = tokenizer.eos_token

    print("Model ready for inference.\n")
    return model, tokenizer


@torch.inference_mode()
def run_inference(model, tokenizer, instruction: str, max_new_tokens: int = 200) -> tuple[str, float]:
    prompt = build_prompt(instruction)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    t0 = time.perf_counter()
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,            # Greedy decoding — deterministic, best for Tcl commands
        temperature=1.0,
        repetition_penalty=1.1,     # Prevents the model looping on the same token
        eos_token_id=tokenizer.eos_token_id,
        pad_token_id=tokenizer.eos_token_id,
    )
    elapsed = time.perf_counter() - t0

    # Decode only the generated tokens (strip the prompt)
    generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()

    return response, elapsed


def run_evaluation(base_model: str, adapters: str):
    model, tokenizer = load_model(base_model, adapters)

    results = []
    total_latency = 0.0

    print("=" * 65)
    print(f"EVALUATION — {len(TEST_QUERIES)} test queries")
    print("=" * 65)

    for idx, query in enumerate(TEST_QUERIES, 1):
        print(f"\n[{idx:02d}/{len(TEST_QUERIES)}] [{query['category']}]")
        print(f"  Q: {query['instruction']}")

        response, latency = run_inference(model, tokenizer, query["instruction"])
        total_latency += latency

        print(f"  A: {response}")
        print(f"  ⏱  {latency:.2f}s")

        results.append({
            "id": idx,
            "category": query["category"],
            "instruction": query["instruction"],
            "response": response,
            "latency_seconds": round(latency, 3),
        })

    # ── Save Results ───────────────────────────────────────────
    Path(RESULTS_DIR).mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = Path(RESULTS_DIR) / f"eval_{timestamp}.json"

    summary = {
        "metadata": {
            "timestamp": timestamp,
            "base_model": base_model,
            "adapters": adapters,
            "num_queries": len(TEST_QUERIES),
            "avg_latency_seconds": round(total_latency / len(TEST_QUERIES), 3),
            "total_latency_seconds": round(total_latency, 3),
        },
        "results": results,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 65)
    print(f"Evaluation complete!")
    print(f"  Queries tested  : {len(TEST_QUERIES)}")
    print(f"  Avg latency     : {total_latency / len(TEST_QUERIES):.2f}s per query")
    print(f"  Results saved   : {out_path}")
    print("=" * 65)

    return out_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate the fine-tuned QLoRA TCL model.")
    parser.add_argument("--base_model", type=str, default=DEFAULT_BASE_MODEL, help="Path to the base model directory.")
    parser.add_argument("--adapters",   type=str, default=DEFAULT_ADAPTERS,   help="Path to the LoRA adapter directory.")
    args = parser.parse_args()

    import os
    os.environ["PYTHONUTF8"] = "1"

    run_evaluation(args.base_model, args.adapters)
