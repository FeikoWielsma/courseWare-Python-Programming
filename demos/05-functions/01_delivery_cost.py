def delivery_cost(total):
    if total >= 50.0:
        return 0.0
    return 4.95


print(delivery_cost(35.0))
print(delivery_cost(75.0))
