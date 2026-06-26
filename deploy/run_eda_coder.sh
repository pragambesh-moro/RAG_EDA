#!/bin/bash
echo "Starting EDA-Coder..."
if [ ! -d "../.venv" ]; then
    echo "Virtual environment not found! Please run install_linux.sh first."
    exit 1
fi
source ../.venv/bin/activate
python3 ../tcl_inference.py
