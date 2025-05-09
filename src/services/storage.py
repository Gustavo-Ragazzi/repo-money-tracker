import sqlite3
from models.session import Session


def get_connection():
    return sqlite3.connect("data/data.db")


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                name TEXT,
                created_at TEXT,
                round INTEGER,
                total_money REAL,
                deleted INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def save_session(session: Session):
    with get_connection() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO sessions
                (id, name, created_at, round, total_money, deleted)
            VALUES
                (?, ?, ?, ?, ?, 0)
            """,
            (
                session.id,
                session.name,
                session.created_at,
                session.round,
                session.total_money,
            ),
        )


def load_sessions():
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id,
                name,
                created_at,
                round,
                total_money
            FROM sessions
            WHERE deleted = 0
            """
        ).fetchall()
        return [Session(*row, players=[], loans=[]) for row in rows]


def soft_delete_session(session_id: str):
    with get_connection() as conn:
        conn.execute("UPDATE sessions SET deleted = 1 WHERE id = ?", (session_id,))
        conn.commit()
