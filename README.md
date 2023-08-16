<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Holocaust spaCy

This is a pipeline designed to work with documents from the Holocaust. It allows users to identify Holocaust-specific data, such as CAMP and GHETTO. Its vectors are also trained on Holocaust-specific data.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `build_floret` | Creates the floret embeddings for the .md model |
| `floret2spacy` | Create a base spaCy pipeline with the floret embeddings |
| `build_rules` | Build Pipeline |
| `train` | Train model |
| `package` | Package the Pipeline |
| `push2hub` | Pushes the new version to HuggingFace Hub |
| `build_corpus` | Downloads the collection of oral testimonies from HuggingFace and then creates a corpus.txt file for training floret embeddings |
| `build_env` | Builds the environment for training on GPU |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all-vectors` | `train` &rarr; `package` &rarr; `push2hub` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/train.json` | Local | Demo training data adapted from the `ner_demo` project |
| `assets/dev.json` | Local | Demo development data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
    