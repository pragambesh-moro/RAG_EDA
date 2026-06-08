import os
import urllib.request
import subprocess

def download_hpc_wheels():
    os.makedirs("hpc_wheels", exist_ok=True)
    
    print("1/2: Downloading PyTorch CUDA 12.1 Linux Wheel directly...")
    torch_url = "https://download.pytorch.org/whl/cu121/torch-2.1.2%2Bcu121-cp311-cp311-linux_x86_64.whl"
    torch_out = "hpc_wheels/torch-2.1.2+cu121-cp311-cp311-linux_x86_64.whl"
    
    if not os.path.exists(torch_out):
        urllib.request.urlretrieve(torch_url, torch_out)
        print("PyTorch download complete!")
    else:
        print("PyTorch wheel already exists, skipping.")
        
    print("\n2/2: Downloading HuggingFace dependencies via pip...")
    # Using pip for the rest since they don't have custom CUDA indices that break pip's cross-platform solver
    cmd = [
        "pip", "download", 
        "transformers", "peft", "trl", "bitsandbytes", "datasets", "accelerate", "triton==2.1.0",
        "--platform", "manylinux2014_x86_64", 
        "--python-version", "3.11", 
        "--only-binary=:all:", 
        "-d", "hpc_wheels"
    ]
    subprocess.run(cmd)
    
    import glob
    print("Cleaning up conflicting PyPI torch wheels...")
    for f in glob.glob("hpc_wheels/torch-2.*"):
        if "cu121" not in f:
            os.remove(f)
            print(f"Removed conflicting PyPI wheel: {f}")
            
    print("\nAll Linux wheels downloaded successfully to the 'hpc_wheels' folder!")

if __name__ == "__main__":
    download_hpc_wheels()
