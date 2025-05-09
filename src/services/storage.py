def save_purchase(
    session_id: str, player_id: int, level_number: int, item: str, price: float
):
    with get_connection() as conn:
        conn.execute(
            """
      INSERT INTO purchases (session_id, player_id, level_number, item, price)
      VALUES (?, ?, ?, ?, ?)
      """,
            (session_id, player_id, level_number, item, price),
        )
        conn.commit()


def record_loan(
    session_id: str,
    from_player_id: int,
    to_player_id: int,
    level_number: int,
    amount: float,
):
    with get_connection() as conn:
        conn.execute(
            """
      INSERT INTO loans (session_id, from_player_id, to_player_id, level_number, amount, applied)
      VALUES (?, ?, ?, ?, ?, 0)
      """,
            (session_id, from_player_id, to_player_id, level_number, amount),
        )
        conn.commit()


def set_player_money_for_level(
    session_id: str, player_id: int, level_number: int, money: float
):
    with get_connection() as conn:
        conn.execute(
            """
      INSERT INTO player_money_per_level (session_id, player_id, level_number, money)
      VALUES (?, ?, ?, ?)
      ON CONFLICT(session_id, player_id, level_number)
      DO UPDATE SET money = excluded.money
      """,
            (session_id, player_id, level_number, money),
        )
        conn.commit()


# ----------------------------
# QUERY FUNCTIONS
# ----------------------------


def get_purchases_by_player(session_id: str, player_id: int):
    with get_connection() as conn:
        rows = conn.execute(
            """
      SELECT level_number, item, price
      FROM purchases
      WHERE session_id = ? AND player_id = ?
      ORDER BY level_number
      """,
            (session_id, player_id),
        ).fetchall()

        return [
            {"level": level, "item": item, "price": price}
            for level, item, price in rows
        ]


def get_loans_for_session(session_id: str):
    with get_connection() as conn:
        rows = conn.execute(
            """
      SELECT from_player_id, to_player_id, level_number, amount, applied
      FROM loans
      WHERE session_id = ?
      ORDER BY level_number
      """,
            (session_id,),
        ).fetchall()

        return [
            {
                "from": from_id,
                "to": to_id,
                "level": level,
                "amount": amount,
                "applied": bool(applied),
            }
            for from_id, to_id, level, amount, applied in rows
        ]
