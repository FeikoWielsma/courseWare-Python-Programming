# The last two lines show the older styles on purpose, for recognising them.

art = 453
price = 59.058
print(f"Art: {art:5d}, Price per Unit: {price:8.2f}")

print(f"[{'Curie':<10}]")  # [Curie     ]
print(f"[{'Curie':^10}]")  # [  Curie   ]
print(f"[{'Curie':>10}]")  # [     Curie]
print(f"{1234567.891:,.2f}")  # 1,234,567.89
print(f"{0.25:.0%}")  # 25%

print("Art: %5d, Price per Unit: %8.2f" % (art, price))
print("Art: {:5d}, Price per Unit: {:8.2f}".format(art, price))
