from dataclasses import dataclass


@dataclass
class Player:
    id: int
    name: str
    is_host: bool
