FREE_SHIPPING: float = 50.0


def delivery_cost(total: float) -> float:
    if total >= FREE_SHIPPING:
        return 0.0
    return 4.95
