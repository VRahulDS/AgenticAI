from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent



OUTPUTS_DIR = ROOT_DIR / "output"

ENV_FPATH = ROOT_DIR.parent.parent / ".env"

APP_CONFIG_FPATH = ROOT_DIR / "config" / "config.yaml"
PROMPT_CONFIG_FPATH = ROOT_DIR / "config" / "prompt_config.yaml"

PUBLICATION_FPATH = ROOT_DIR / "published_data.txt"