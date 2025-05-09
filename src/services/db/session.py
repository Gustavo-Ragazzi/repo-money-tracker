from typing import List
from .db_connection import get_connection
from models.session import Session
from datetime import datetime


def get_active_sessions() -> List[Session]:
  with get_connection() as conn:
    rows = conn.execute("""
      SELECT id, name, actual_level, total_money, is_finished, deleted, created_at
      FROM sessions
      WHERE is_finished = 0 AND deleted = 0
      ORDER BY created_at DESC
    """).fetchall()
    return [Session.from_row(row) for row in rows]


def create_session(name: str, player_names: list[str]) -> int:
  with get_connection() as conn:
    cursor = conn.cursor()
    created_at = datetime.now().isoformat(timespec="seconds")

    cursor.execute(
      """
      INSERT INTO sessions (name, actual_level, total_money, is_finished, deleted, created_at)
      VALUES (?, ?, ?, ?, ?, ?)
      """,
      (name, 1, 0.0, 0, 0, created_at)
    )
    session_id = cursor.lastrowid

    for i, player_name in enumerate(player_names):
      if not player_name.strip():
        continue
      cursor.execute(
        """
        INSERT INTO players (session_id, name, is_host, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (session_id, player_name.strip(), int(i == 0), created_at)
      )

    conn.commit()
    return session_id


def delete_session(session_id: int):
  with get_connection() as conn:
    conn.execute("UPDATE sessions SET deleted = 1 WHERE id = ?", (session_id,))
    conn.commit()


def finish_session(session_id: int):
  with get_connection() as conn:
    conn.execute("UPDATE sessions SET is_finished = 1 WHERE id = ?", (session_id,))
    conn.commit()
