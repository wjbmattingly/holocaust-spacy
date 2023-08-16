import spacy
import argparse
from components import *
import glob
import os
from typing import List, Dict

def create_patterns(filename: str) -> List[Dict[str, str]]:
    """
    Create a list of patterns from a given text file.

    :param filename: Path to the text file containing the patterns.
    :return: A list of dictionaries containing the pattern and its corresponding label.
    """
    try:
        base_name = os.path.basename(filename)
        label, _ = os.path.splitext(base_name)
        label = label.upper()
        print(f"Building patterns for {label}")
        with open(filename, "r", encoding="utf-8") as f:
            phrases = f.read().splitlines()
        patterns = []
        for phrase in phrases:
            tokens = phrase.split()
            pattern = [{"LOWER": token.lower()} for token in tokens]
            patterns.append({"pattern": pattern, "label": label})
        return patterns
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occurred while processing {filename}: {str(e)}")
        return []


def build(name, version, description, author, output_directory, lang):
    nlp = spacy.blank(lang)
    # ruler = nlp.add_pipe("span_ruler", config= {"spans_key":"sc"})
    ruler = nlp.add_pipe("entity_ruler")

    pattern_files = glob.glob("assets/patterns/*.txt")

    patterns = []
    for filename in pattern_files:
        patterns = patterns+create_patterns(filename)
    ruler.add_patterns(patterns)

    nlp.add_pipe("find_ghettos")

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
