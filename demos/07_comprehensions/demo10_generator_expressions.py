numbers = [4, 8, 15, 16, 23, 42]
print(sum(n * n for n in numbers))  # 2854
print(any(n > 40 for n in numbers))  # True
print(all(n % 2 == 0 for n in numbers))  # False
print(any([]), all([]))  # False True
