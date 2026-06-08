#!/bin/bash
#SBATCH --job-name=qlora_tcl_train
#SBATCH -p gpu
#SBATCH --gres=gpu:nvidia_a100_80gb_pcie_1g.10gb:1
#SBATCH -c 4
#SBATCH -t 24:00:00
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

echo "Starting Slurm Job: $SLURM_JOB_ID"
echo "Node allocated: $SLURM_JOB_NODELIST"

# Load necessary modules per HPC availability
module load cuda/12.8
module load python/3.11.11-cuda

# Activate the virtual environment
# Ensure this matches the absolute path to your venv on the HPC
source ~/venvs/project/bin/activate

# Execute the QLoRA training script
# Note: Ensure the base model (e.g., DeepSeek-Coder) is pre-downloaded 
# to a local HPC directory if there is no outbound internet access.
python qlora_train.py

echo "Job Finished."
