import spacy
import argparse
from components import *

def build(name, version, description, author, output_directory, lang):
    nlp = spacy.blank(lang)

    nlp.meta["name"] = name
    nlp.meta["version"] = version
    nlp.meta["description"] = description
    nlp.meta["author"] = author

    nlp.to_disk(output_directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build the NLP pipeline.')
    parser.add_argument('--name', type=str, required=True, help='Name of the pipeline.')
    parser.add_argument('--version', type=str, required=True, help='Version of the pipeline.')
    parser.add_argument('--description', type=str, required=True, help='Description of the pipeline.')
    parser.add_argument('--author', type=str, required=True, help='Author of the pipeline.')
    parser.add_argument('--output_directory', type=str, required=True, help='Output directory for the pipeline.')
    parser.add_argument('--lang', type=str, required=True, help='Language code for the pipeline.')
    
    args = parser.parse_args()
    
    build(args.name, args.version, args.description, args.author, args.output_directory, args.lang)
