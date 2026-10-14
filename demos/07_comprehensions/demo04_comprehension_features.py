def subtract(a: int, b: int) -> int:
    return a - b


pairs = [(6, 3), (1, 7), (5, 5)]
differences = [subtract(y, x) for x, y in pairs]
print(differences)  # [-3, 6, 0]
