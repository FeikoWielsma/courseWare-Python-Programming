squares = {number: number**2 for number in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
counts = {"a": 2, "b": 0, "c": 3}
positive = {key.upper(): value for key, value in counts.items() if value > 0}
print(positive)  # {'A': 2, 'C': 3}
