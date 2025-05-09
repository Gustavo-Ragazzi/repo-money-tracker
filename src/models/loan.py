from dataclasses import dataclass


@dataclass
class Loan:
    to: str
    ammount: int
    from_player: str
    applied: bool
