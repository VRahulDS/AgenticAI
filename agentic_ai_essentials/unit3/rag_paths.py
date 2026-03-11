from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

LOG_DIR = ROOT_DIR / "logs"
LOG_FPATH = LOG_DIR / "app.logs"

CODE_DIR = ROOT_DIR / "src"

DATA_DIR = ROOT_DIR / "data"

DB_DIR = ROOT_DIR / "DB"

ENV_FPATH = ROOT_DIR.parent / ".env"

PROMPT_CONFIG_FPATH = ROOT_DIR / "src" / "config" / "prompt_config.yaml"

APP_CONFIG_FPATH = ROOT_DIR / "src" / "config" / "config.yaml"
