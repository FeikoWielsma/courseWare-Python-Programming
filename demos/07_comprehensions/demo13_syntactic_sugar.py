mapped = list(map(lambda x: 2 * x + 1, [10, 20, 30]))
print(mapped)  # [21, 41, 61]
comprehended = [2 * x + 1 for x in [10, 20, 30]]
print(comprehended)  # [21, 41, 61]
