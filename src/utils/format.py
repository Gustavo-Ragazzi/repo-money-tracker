from datetime import datetime

def format_datetime(iso_str: str) -> str:
  return datetime.fromisoformat(iso_str).strftime("%d/%m/%Y %H:%M")
