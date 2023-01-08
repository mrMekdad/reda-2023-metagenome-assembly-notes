"""Core workflow for Metagenome Assembly Notes by Red@."""

PROJECT_NAME = "Metagenome Assembly Notes"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
