
"""Risk calculations with a hard 1% planned-risk ceiling."""

MAX_RISK_PERCENT = 1.0


def calculate_risk_amount(
    account_equity: float,
    risk_percent: float = 1.0,
) -> float:
    """Calculate a risk budget; never execute an order."""

    if (
        isinstance(account_equity, bool)
        or not isinstance(account_equity, (int, float))
    ):
        raise ValueError("account_equity must be a number")

    if account_equity <= 0:
        raise ValueError("account_equity must be greater than zero")

    if (
        isinstance(risk_percent, bool)
        or not isinstance(risk_percent, (int, float))
    ):
        raise ValueError("risk_percent must be a number")

    if risk_percent <= 0:
        raise ValueError("risk_percent must be greater than zero")

    if risk_percent > MAX_RISK_PERCENT:
        raise ValueError("risk_percent cannot exceed the 1% hard limit")

    return float(account_equity) * float(risk_percent) / 100.0
