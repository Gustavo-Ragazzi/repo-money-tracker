from .db_connection import get_connection


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                actual_level INTEGER NOT NULL DEFAULT 1, -- current level number
                total_money REAL NOT NULL,
                is_finished INTEGER NOT NULL DEFAULT 0,  -- 0 = ongoing, 1 = finished
                deleted INTEGER NOT NULL DEFAULT 0,
                created_at DATETIME NOT NULL
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slot INTEGER NOT NULL,
                session_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                is_host INTEGER NOT NULL DEFAULT 0,
                created_at DATETIME NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
                UNIQUE(session_id, slot)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS levels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                number INTEGER NOT NULL,
                previous_remaining_money REAL NOT NULL,  -- leftover previous level
                collected_money REAL NOT NULL,           -- collected money this level
                total_available REAL NOT NULL,           -- sum of previous + collected
                created_at DATETIME NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE,
                UNIQUE(session_id, number)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS player_level_state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                level_id INTEGER NOT NULL,
                player_id INTEGER NOT NULL,
                purchases_json TEXT,                      -- list of items and prices
                loans_given_json TEXT,                    -- list of donations made
                total_donated REAL NOT NULL DEFAULT 0.0,  -- total given to others
                total_received REAL NOT NULL DEFAULT 0.0, -- total received from others
                previous_remaining REAL NOT NULL,         -- left from previous level
                post_donation_balance REAL NOT NULL,      -- prev + received - donated
                final_balance REAL NOT NULL,              -- computed value
                created_at DATETIME NOT NULL,
                FOREIGN KEY (level_id) REFERENCES levels(id) ON DELETE CASCADE,
                FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
            )
            """
        )

        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_player_session ON players(session_id)
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_level_session ON levels(session_id)
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_state_level ON player_level_state(level_id)
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_state_player ON player_level_state(player_id)
            """
        )

        conn.commit()
