def line_total(price: float, quantity: int) -> float:
    return round(price * quantity, 2)


items = [(12.50, 2), (4.00, 3), (7.25, 1)]
totals = [line_total(price, quantity) for price, quantity in items]
print(totals)  # [25.0, 12.0, 7.25]
