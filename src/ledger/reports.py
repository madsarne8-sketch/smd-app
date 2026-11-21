"""Financial calculations on transactions."""

from collections import defaultdict
from collections.abc import Callable, Iterable
from decimal import Decimal

from ledger.models import Transaction

TRANSFER = "transfer"


def totals_by(
    transactions: Iterable[Transaction],
    key: Callable[[Transaction], str],
) -> dict[str, Decimal]:
    """Calculate totals grouped by a selected key."""
    totals: dict[str, Decimal] = defaultdict(Decimal)

    for t in transactions:
        totals[key(t)] += t.amount

    return dict(totals)


def is_spending(t: Transaction) -> bool:
    """Return True for outgoing money, excluding transfers."""
    return t.amount < 0 and t.category != TRANSFER


def balances(
    transactions: Iterable[Transaction],
) -> dict[str, Decimal]:
    """Calculate the balance of each account."""
    totals = totals_by(
        transactions,
        key=lambda t: t.account,
    )
    return dict(sorted(totals.items()))


def spending_by_category(
    transactions: Iterable[Transaction],
) -> dict[str, Decimal]:
    """Calculate spending by category as positive amounts."""
    spending = [
        t for t in transactions if is_spending(t)
    ]

    totals = totals_by(
        spending,
        key=lambda t: t.category,
    )

    return {
        category: -total
        for category, total in sorted(
            totals.items(),
            key=lambda item: item[1],
        )
    }
