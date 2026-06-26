#!/bin/bash
echo "=========================================="
echo " Setting up EDA Coder Benchmark on Mac"
echo "=========================================="

echo "[1/4] Installing dependencies..."
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_inference.txt

echo "[2/4] Pulling DeepSeek Base Model..."
ollama pull deepseek-coder:6.7b-base

echo "[3/4] Importing Custom EDA Coder to Ollama..."
ollama create eda-coder -f Modelfile

echo "[4/4] Setup Complete!"
echo "Run the benchmark with: python run_missing_benchmark.py"
echo "=========================================="
