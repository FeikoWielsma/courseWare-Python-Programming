def print_receipt(product, unit_price, quantity):
    total = unit_price * quantity
    print(f"{quantity} x {product}: {total:.2f}")


print_receipt("Keyboard", 25.0, 2)
print_receipt("Mouse", 15.0, 1)
