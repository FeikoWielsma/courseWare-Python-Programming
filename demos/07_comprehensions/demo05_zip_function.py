products = ["tea", "coffee", "cocoa"]
quantities = [12, 8, 5]
pairs = list(zip(products, quantities))
print(pairs)  # [('tea', 12), ('coffee', 8), ('cocoa', 5)]
checked = list(zip(products, quantities, strict=True))
print(checked)  # [('tea', 12), ('coffee', 8), ('cocoa', 5)]
