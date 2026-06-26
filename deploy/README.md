# EDA-Coder Deployment Guide

This folder contains the scripts needed to install and run EDA-Coder on your local machine or server.

## Installation
Run the installation script for your OS. This will set up the Python virtual environment, install dependencies, and download the necessary models into Ollama.

**Windows:**
```powershell
.\install_windows.ps1
```

**Linux/Mac:**
```bash
chmod +x install_linux.sh
./install_linux.sh
```

## Running the Copilot
Once installed, use the runner script to automatically launch the interactive EDA-Coder assistant.

**Windows:**
```powershell
.\run_eda_coder.ps1
```

**Linux/Mac:**
```bash
chmod +x run_eda_coder.sh
./run_eda_coder.sh
```
