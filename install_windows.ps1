Write-Host "================================================="
Write-Host "  EDA Coder Local Deployment (Windows)"
Write-Host "================================================="

# 1. Check for Ollama
if (-not (Get-Command "ollama" -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Ollama is not installed." -ForegroundColor Red
    Write-Host "Please download and install Ollama from https://ollama.com/download/windows"
    exit 1
}

Write-Host "[1/4] Checking Ollama service..."
$ollamaRunning = Get-Process "ollama" -ErrorAction SilentlyContinue
if (-not $ollamaRunning) {
    Write-Host "Please ensure the Ollama app is running in your system tray." -ForegroundColor Yellow
}

# 2. Inject the model into Ollama
Write-Host "[2/4] Importing GGUF model into local Ollama registry..."
if (-not (Test-Path "Modelfile") -or -not (Test-Path "deepseek-synopsys-7b-Q4_K_M.gguf")) {
    Write-Host "ERROR: Missing Modelfile or GGUF model in the current directory." -ForegroundColor Red
    exit 1
}
ollama create eda-coder -f Modelfile

# 3. Setup Python Virtual Environment
Write-Host "[3/4] Setting up Python virtual environment..."
if (-not (Get-Command "python" -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python is not installed." -ForegroundColor Red
    exit 1
}

python -m venv .venv
$env:VIRTUAL_ENV = "$PWD\.venv"
$env:Path = "$PWD\.venv\Scripts;$env:Path"

# 4. Install Dependencies
Write-Host "[4/4] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements_inference.txt

Write-Host "=================================================" -ForegroundColor Green
Write-Host "  Success! Deployment Complete." -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green
Write-Host "To chat with your model, simply run:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  python tcl_inference.py"
Write-Host "================================================="
