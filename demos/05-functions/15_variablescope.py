delivery_fee = 4.95
free_from = 50.0


def preview_fee() -> None:
    delivery_fee = 0.0
    print(f"Preview fee: {delivery_fee:.2f}")


def set_threshold() -> None:
    global free_from
    free_from = 75.0


preview_fee()
print(f"Current fee: {delivery_fee:.2f}")
set_threshold()
print(f"Free from: {free_from:.2f}")
