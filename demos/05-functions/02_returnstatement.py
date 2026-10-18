def delivery_cost(total):
    if total >= 50.0:
        return 0.0
    return 4.95


shipping = delivery_cost(35.0)
grand_total = 35.0 + shipping
print(f"Order total: {grand_total:.2f}")
