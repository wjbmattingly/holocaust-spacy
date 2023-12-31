from spacy.cli.project.run import project_run
from spacy.cli.project.assets import project_assets
from pathlib import Path


def project():
    root = Path(__file__).parent
    project_assets(root)
    project_run(root, "all", capture=True)
    project_run(root, "all-vectors", capture=True)
    project_run(root, "package", capture=True)