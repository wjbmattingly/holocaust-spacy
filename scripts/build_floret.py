import floret
import argparse
import os

def create_floret(corpus_file, floret_file, overwrite=False):
    if os.path.exists(floret_file) and not overwrite:
        print(f"{floret_file} already exists. Use --overwrite to overwrite the existing file.")
        return

    model = floret.train_unsupervised(
        corpus_file,
        model="cbow",
        mode="floret",
        hashCount=2,
        bucket=50000,
        minn=3,
        maxn=6,
    )

    # Export floret vector table
    model.save_floret_vectors(floret_file)
    print(f"Floret vectors saved to {floret_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Floret embeddings.")
    parser.add_argument("corpus_file", type=str, help="Path to the corpus file.")
    parser.add_argument("floret_file", type=str, help="Path to save the Floret vectors.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the existing file if it exists.")

    args = parser.parse_args()
    create_floret(args.corpus_file, args.floret_file, args.overwrite)
