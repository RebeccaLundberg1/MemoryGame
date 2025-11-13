from __future__ import annotations
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
SAVE_PATH = DATA_DIR / "saveGame.json"
TOPLIST_PATH = DATA_DIR / "toplist.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)

def read_db(filetype: str) -> dict:
    """Read JSON database. Returns empty list if file doesn't exist or är invalid."""
    filetype = filetype.upper()
    if filetype != "SAVE" and filetype != "TOPLIST":
        raise ValueError(f"Invalid filetype: {filetype}. Must be 'SAVE' or 'TOPLIST'.")
    
    path = SAVE_PATH if filetype == "SAVE" else TOPLIST_PATH
    if not path.exists():
        if filetype == "TOPLIST":
            return {"easy": [], "medium": [], "hard": [], "extreme": []}
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, IOError):
        return {}

def write_db(items: dict, filetype: str) -> None:
    """Write items to JSON database."""
    filetype = filetype.upper()
    if filetype != "SAVE" and filetype != "TOPLIST":
        raise ValueError (f"Invalid filetype: {filetype}. Must be 'SAVE' or 'TOPLIST'.")
    if not isinstance(items, dict):
        raise ValueError("Database must be a dict")
    
    path = SAVE_PATH if filetype == "SAVE" else TOPLIST_PATH
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)