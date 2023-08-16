import json
import argparse

def update_meta_file(path, **kwargs):
    updatable_keys = [
        "lang", "name", "version", "spacy_version",
        "description", "author", "email", "url", "license"
    ]

    with open(path, 'r') as file:
        meta_data = json.load(file)

    for key, value in kwargs.items():
        if key in updatable_keys:
            meta_data[key] = value

    with open(path, 'w') as file:
        json.dump(meta_data, file, indent=2)

    print(f"Updated {path} with the provided values.")

def main():
    parser = argparse.ArgumentParser(description='Update meta.json file')
    parser.add_argument('path', type=str, help='Path to the meta.json file')
    parser.add_argument('--lang', type=str, help='Language')
    parser.add_argument('--name', type=str, help='Name')
    parser.add_argument('--version', type=str, help='Version')
    parser.add_argument('--spacy_version', type=str, help='Spacy version')
    parser.add_argument('--description', type=str, help='Description')
    parser.add_argument('--author', type=str, help='Author')
    parser.add_argument('--email', type=str, help='Email')
    parser.add_argument('--url', type=str, help='URL')
    parser.add_argument('--license', type=str, help='License')

    args = parser.parse_args()
    kwargs = {k: v for k, v in vars(args).items() if v is not None and k != 'path'}

    update_meta_file(args.path, **kwargs)

if __name__ == '__main__':
    main()
