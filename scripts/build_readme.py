import argparse
import yaml

def build(yml_content, readme_file):
    workflow_table = format_workflows(yml_content)
    commands_table = format_commands(yml_content)
    assets_table = format_assets(yml_content)

    title = yml_content.get('title', '')
    description = yml_content.get('description', '')
    yml_description = yml_content.get('yml_description', '')

    text = f"""<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: {title}

{description}

## 📋 project.yml
{yml_description}

### ⏯ Commands

{commands_table}


### ⏭ Workflows

{workflow_table}

### 🗂 Assets

{assets_table}

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
    """
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(text)


def format_commands(yml_content):
    commands = yml_content['commands']
    table = "| Command | Description |\n| --- | --- |"
    for command in commands:
        name = command['name']
        description = command['help']
        table += f"\n| `{name}` | {description} |"
    return table
    

def format_workflows(yml_content):
    workflows = yml_content['workflows']
    table = "| Workflow | Steps |\n| --- | --- |"
    for workflow_name, steps in workflows.items():
        steps_str = " &rarr; ".join(f'`{step}`' for step in steps)
        table += f"\n| `{workflow_name}` | {steps_str} |"
    return table

def format_assets(yml_content):
    assets = yml_content['assets']
    table = "| File | Source | Description |\n| --- | --- | --- |"
    for asset in assets:
        dest = asset['dest']
        description = asset['description']
        table += f'\n| [`{dest}`]({dest}) | Local | {description} |'
    return table


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build the NLP pipeline.')
    parser.add_argument('--yaml_file', type=str, required=True, help="The project's yml file")
    parser.add_argument('--readme_file', type=str, required=True, help="The output readme file")
    args = parser.parse_args()
    with open(args.yaml_file, 'r') as file:
        yml_content = yaml.safe_load(file)
    build(yml_content, args.readme_file)
    