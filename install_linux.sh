#!/bin/bash
set -e

echo "================================================="
echo "  EDA Coder Local Deployment (Linux)"
echo "================================================="

# 1. Check for Ollama
if ! command -v ollama &> /dev/null
then
    echo "ERROR: Ollama is not installed."
    echo "Please install Ollama first by running: curl -fsSL https://ollama.com/install.sh | sh"
    exit 1
fi

echo "[1/4] Checking Ollama service..."
if ! systemctl is-active --quiet ollama && ! pgrep -x "ollama" > /dev/null; then
    echo "Starting Ollama service in the background..."
    ollama serve > /dev/null 2>&1 &
    sleep 3
fi

# 2. Inject the model into Ollama
echo "[2/4] Importing GGUF model into local Ollama registry..."
if [ ! -f "Modelfile" ] || [ ! -f "deepseek-synopsys-7b-Q4_K_M.gguf" ]; then
    echo "ERROR: Missing Modelfile or GGUF model in the current directory."
    exit 1
fi
ollama create eda-coder -f Modelfile

# 3. Setup Python Virtual Environment
echo "[3/4] Setting up Python virtual environment..."
if ! command -v python3 &> /dev/null
then
    echo "ERROR: python3 is not installed."
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate

# 4. Install Dependencies
echo "[4/4] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements_inference.txt

echo "================================================="
echo "  Success! Deployment Complete."
echo "================================================="
echo "To chat with your model, simply run:"
echo "  source .venv/bin/activate"
echo "  python tcl_inference.py"
echo "================================================="
