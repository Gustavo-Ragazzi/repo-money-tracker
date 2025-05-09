from typing import List, Optional
from .db_connection import get_connection
from models.session import Session, SessionFullData, PlayerWithState, PlayerLevelState
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

def get_session_full_data(session_id: int) -> Optional[SessionFullData]:
  with get_connection() as conn:
    rows = conn.execute(
      """
      SELECT
        s.id, s.name, s.actual_level, s.total_money, s.is_finished, s.deleted, s.created_at,
        p.id, p.name, p.is_host, p.created_at,
        l.id, l.previous_remaining_money, l.collected_money, l.total_available,
        pls.purchases_json, pls.loans_given_json, pls.total_donated, pls.total_received,
        pls.previous_remaining, pls.post_donation_balance, pls.final_balance
      FROM sessions s
      LEFT JOIN players p ON p.session_id = s.id
      LEFT JOIN levels l ON l.session_id = s.id AND l.number = s.actual_level
      LEFT JOIN player_level_state pls ON pls.level_id = l.id AND pls.player_id = p.id
      WHERE s.id = ?
      """,
      (session_id,)
    ).fetchall()

  if not rows:
    return None

  session_row = rows[0]
  session = SessionFullData(
    id=session_row[0],
    name=session_row[1],
    actual_level=session_row[2],
    total_money=session_row[3],
    is_finished=bool(session_row[4]),
    deleted=bool(session_row[5]),
    created_at=session_row[6],
    level_id=session_row[11],
    previous_remaining_money=session_row[12],
    collected_money=session_row[13],
    total_available=session_row[14],
    players=[]
  )

  for row in rows:
    if row[7] is None:
      continue

    if row[15] is not None:
      level_state = PlayerLevelState(
        purchases_json=row[15],
        loans_given_json=row[16],
        total_donated=row[17],
        total_received=row[18],
        previous_remaining=row[19],
        post_donation_balance=row[20],
        final_balance=row[21],
      )
    else:
      level_state = None

    player = PlayerWithState(
      id=row[7],
      name=row[8],
      is_host=bool(row[9]),
      created_at=row[10],
      level_state=level_state
    )
    session.players.append(player)

  return session


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
