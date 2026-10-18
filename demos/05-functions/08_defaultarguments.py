def delivery_cost(total: float, free_from: float = 50.0) -> float:
    if total >= free_from:
        return 0.0
    return 4.95


print(delivery_cost(35.0))
print(delivery_cost(35.0, free_from=30.0))
