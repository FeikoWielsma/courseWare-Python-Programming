def delivery_cost(total: float) -> float:
    if total >= 50.0:
        return 0.0
    return 4.95


def print_receipt(product: str, unit_price: float, quantity: int) -> None:
    total = unit_price * quantity
    print(f"{quantity} x {product}: {total:.2f}")


print(delivery_cost(35.0))
print_receipt("Keyboard", 25.0, 2)
