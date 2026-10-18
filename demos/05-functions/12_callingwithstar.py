def delivery_cost(total: float, free_from: float) -> float:
    if total >= free_from:
        return 0.0
    return 4.95


order = (35.0, 50.0)
print(delivery_cost(*order))

options = {"total": 75.0, "free_from": 50.0}
print(delivery_cost(**options))
