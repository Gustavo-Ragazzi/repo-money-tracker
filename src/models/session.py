from dataclasses import dataclass
from models.player import Player
from models.loan import Loan
from typing import List

@dataclass
class Session:
    id: str 
    name: str
    created_at: str
    round: int
    total_money: float
    players: List[Player]
    loans: List[Loan]
