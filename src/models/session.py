from dataclasses import dataclass
from typing import Optional


@dataclass
class Session:
    id: int
    name: str
    actual_level: int
    total_money: float
    is_finished: bool
    deleted: bool
    created_at: str

    @staticmethod
    def from_row(row: tuple) -> "Session":
        return Session(
            id=row[0],
            name=row[1],
            actual_level=row[2],
            total_money=row[3],
            is_finished=bool(row[4]),
            deleted=bool(row[5]),
            created_at=row[6],
        )

@dataclass
class PlayerLevelState:
  purchases_json: Optional[str]
  loans_given_json: Optional[str]
  total_donated: float
  total_received: float
  previous_remaining: float
  post_donation_balance: float
  final_balance: float

@dataclass
class PlayerWithState:
  id: int
  name: str
  is_host: bool
  created_at: str
  level_state: Optional[PlayerLevelState]

@dataclass
class SessionFullData:
  id: int
  name: str
  actual_level: int
  total_money: float
  is_finished: bool
  deleted: bool
  created_at: str
  level_id: int
  previous_remaining_money: float
  collected_money: float
  total_available: float
  players: list[PlayerWithState]
