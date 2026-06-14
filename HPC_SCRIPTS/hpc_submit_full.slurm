#!/bin/bash
#SBATCH --job-name=qlora_tcl_full
#SBATCH -p gpu
#SBATCH --gres=gpu:nvidia_a100_80gb_pcie_7g.80gb:1
#SBATCH -c 16
#SBATCH --mem=256G
#SBATCH -t 24:00:00
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

echo "=================================================="
echo "Starting Full A100 QLoRA Training Job: $SLURM_JOB_ID"
echo "Node allocated: $SLURM_JOB_NODELIST"
echo "GPUs allocated: $CUDA_VISIBLE_DEVICES"
echo "=================================================="

# Load necessary modules
module load cuda/12.8
module load python/3.11.11-cuda

# Activate the virtual environment
source /data/home/pm944/envs/venv/bin/activate

# Force UTF-8 to prevent encoding crashes on Linux too
export PYTHONUTF8=1

# Execute the full-GPU training script
python /data/home/pm944/qlora_train_hpc_full.py

echo "=================================================="
echo "Job Finished: $SLURM_JOB_ID"
echo "=================================================="
