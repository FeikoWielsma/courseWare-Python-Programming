orders = [("A104", 35.0), ("A105", 75.0), ("A106", 20.0)]
by_total = sorted(orders, key=lambda order: order[1])
print(by_total)
