from dataclasses import dataclass
from models.item import Item
from typing import List, Optional


@dataclass
class Purchase:
    item: Item
    price: int
    round: int


@dataclass
class Player:
    name: str
    money: float
    items: List[Purchase]
    is_host: Optional[bool] = False
