from shipping import delivery_cost

order_totals = [35.0, 75.0]
for total in order_totals:
    fee = delivery_cost(total)
    print(f"Order {total:.2f}: delivery {fee:.2f}")
