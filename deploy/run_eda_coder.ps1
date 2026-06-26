Write-Host "Starting EDA-Coder..."
if (-Not (Test-Path "..\.venv")) {
    Write-Host "Virtual environment not found! Please run install_windows.ps1 first." -ForegroundColor Red
    exit
}
..\.venv\Scripts\Activate.ps1
python ..\tcl_inference.py
