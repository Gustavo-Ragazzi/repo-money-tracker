from dataclasses import dataclass


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
