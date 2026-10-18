def delivery_cost(total: float, free_from: float) -> float:
    if total >= free_from:
        return 0.0
    return 4.95


print(delivery_cost(free_from=50.0, total=35.0))
