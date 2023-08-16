import subprocess
import argparse

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("Error executing command:", command)
        print(result.stderr.decode())
        exit(1)
    else:
        print(result.stdout.decode())

def main(env_name, python_version, cuda_version):

    command = (
        f"conda create --name {env_name} python={python_version} -y && "
        f"conda activate {env_name} && "
        f"pip install -U pip setuptools wheel && "
        f"pip install -U spacy[cuda-autodetect] &&"
        f"pip install spacy-huggingface-hub"
    )

    run_command(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create and configure a conda environment")
    parser.add_argument("--env_name", required=True, help="Name of the conda environment to create")
    parser.add_argument("--python_version", required=True, help="Python version for the conda environment")
    parser.add_argument("--cuda_version", required=False, help="CUDA Toolkit version to install")

    args = parser.parse_args()

    main(args.env_name, args.python_version, args.cuda_version)
