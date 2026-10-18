def delivery_cost(total: float) -> float:
    """Return the delivery charge; orders of 50 or more ship free."""
    if total >= 50.0:
        return 0.0
    return 4.95


print(delivery_cost(35.0))
print(delivery_cost.__doc__)
