"""Reading transactions from a CSV file."""

import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

from ledger.models import Transaction


def read_csv(path: Path) -> list[Transaction]:
    """Read a CSV file into Transaction objects."""
    with open(path, newline="") as f:
        return [
            Transaction(
                date=date.fromisoformat(row["date"]),
                account=row["account"],
                description=row["description"],
                category=row["category"],
                amount=Decimal(row["amount"]),
            )
            for row in csv.DictReader(f)
        ]
