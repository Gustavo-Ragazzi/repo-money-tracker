from typing import List
from .db_connection import get_connection
from models.player import Player

def get_players_by_session_id(session_id: int) -> List[Player]:
  with get_connection() as conn:
    rows = conn.execute(
      """
      SELECT id, name, is_host
      FROM players
      WHERE session_id = ?
      ORDER BY id ASC
      """,
      (session_id,)
    ).fetchall()

  return [Player(id=row[0], name=row[1], is_host=bool(row[2])) for row in rows]
