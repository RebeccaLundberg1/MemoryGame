from __future__ import annotations
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "db.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)

def read_db(filename: Path | str = None) -> list[dict]:
    """Read JSON database. Returns empty list if file doesn't exist or är invalid."""
    path = Path(filename) if filename else DB_PATH
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []

def write_db(items: list[dict], filename: Path | str = None) -> None:
    """Write items to JSON database."""
    if not isinstance(items, list):
        raise ValueError("Database must be a list")
    path = Path(filename) if filename else DB_PATH
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)