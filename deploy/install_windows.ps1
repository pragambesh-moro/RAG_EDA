Write-Host "=========================================="
Write-Host " Setting up EDA Coder Benchmark on Windows"
Write-Host "=========================================="

Write-Host "[1/4] Installing dependencies..."
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements_inference.txt

Write-Host "`n[2/4] Pulling DeepSeek Base Model..."
ollama pull deepseek-coder:6.7b-base

Write-Host "`n[3/4] Importing Custom EDA Coder to Ollama..."
ollama create eda-coder -f Modelfile

Write-Host "`n[4/4] Setup Complete!"
Write-Host "Run the benchmark with: python run_missing_benchmark.py"
Write-Host "=========================================="
