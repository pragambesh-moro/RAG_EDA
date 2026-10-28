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

"""
evaluate_model.py — Inference & Evaluation for the Ollama GGUF Model

Tests the Ollama deployed model against a curated set of EDA queries,
records outputs, latency, and saves a timestamped JSON results file.

Usage:
    python evaluate_model.py
    python evaluate_model.py --model eda-coder
"""

import json
import time
import argparse
import requests
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# Defaults
# ─────────────────────────────────────────────
DEFAULT_MODEL = "eda-coder"
RESULTS_DIR   = "./eval_results"

# ─────────────────────────────────────────────
# Test Suite
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


def run_inference(model_name: str, instruction: str) -> tuple[str, float]:
    url = "http://localhost:11434/api/generate"
    # Ollama handles the prompt template (set in Modelfile), so we just pass the instruction.
    payload = {
        "model": model_name,
        "system": "You are an expert Synopsys EDA physical design assistant. You must output ONLY the precise Tcl command requested. Do not provide explanations, markdown formatting, or preamble.",
        "prompt": instruction,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "top_p": 0.95,
        }
    }

    t0 = time.perf_counter()
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        generated_text = data.get("response", "").strip()
    except Exception as e:
        generated_text = f"ERROR: {str(e)}"

    elapsed = time.perf_counter() - t0
    return generated_text, elapsed


def run_evaluation(model_name: str):
    results = []
    total_latency = 0.0

    print("=" * 65)
    print(f"EVALUATION — {len(TEST_QUERIES)} test queries via Ollama API")
    print(f"Model: {model_name}")
    print("=" * 65)

    for idx, query in enumerate(TEST_QUERIES, 1):
        print(f"\n[{idx:02d}/{len(TEST_QUERIES)}] [{query['category']}]")
        print(f"  Q: {query['instruction']}")

        response, latency = run_inference(model_name, query["instruction"])
        total_latency += latency

        print(f"  A: {response}")
        print(f"  [Latency] {latency:.2f}s")

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
            "model_name": model_name,
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
    parser = argparse.ArgumentParser(description="Evaluate the deployed Ollama TCL model.")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="Name of the Ollama model to evaluate.")
    args = parser.parse_args()

    # Check if Ollama is running
    try:
        requests.get("http://localhost:11434")
    except requests.exceptions.ConnectionError:
        print("\nERROR: Could not connect to Ollama.")
        print("Please ensure Ollama is running in the background.")
        exit(1)

    run_evaluation(args.model)
