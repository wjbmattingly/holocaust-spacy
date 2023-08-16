from huggingface_hub import hf_hub_download
import os
import pandas as pd
import spacy

import requests

def download_testimonies():
    local_dir = "corpus/"
    filename = "ushmm_oral_testimonies.csv"
    file_path = os.path.join(local_dir, filename)

    # Check if the directory exists, if not create it
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Check if the file exists in the specified directory
    if not os.path.exists(file_path):
        # If not, download the file
        print(f"{filename} not found. Downloading from Hugging Face Hub...")
        url = "https://huggingface.co/datasets/wjbmattingly/ushmm-testimonies/resolve/main/" + filename
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"{filename} has been downloaded successfully.")
        else:
            print(f"Failed to download {filename}. Please check the URL and try again.")
    else:
        print(f"{filename} already exists in the directory.")



def create_corpus():
    corpus_file_path = "corpus/corpus.txt"

    # Check if the file exists
    if os.path.exists(corpus_file_path):
        print(f"{corpus_file_path} exist. Skipping corpus creation.")
    else:
        
        print("Building corpus...")

        nlp = spacy.blank("en")
        nlp.add_pipe("sentencizer")

        df = pd.read_csv("corpus/ushmm_oral_testimonies.csv")
        df.dropna(subset=["text"], inplace=True)

        texts = df['text'].tolist()

        docs = [nlp(text) for text in texts]
        sents = [str(sent.text) for doc in docs for sent in doc.sents] # Convert spaCy span to string

        with open(corpus_file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(sents))


if __name__ == "__main__":
    download_testimonies()
    create_corpus()
