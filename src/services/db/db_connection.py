import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[3] / "data" / "data.db"
print(DB_PATH)

def get_connection():
  DB_PATH.parent.mkdir(parents=True, exist_ok=True)
  return sqlite3.connect(DB_PATH)
