def square(x: int) -> int:
    return x * x


def even(x: int) -> bool:
    return x % 2 == 0


print(list(map(square, range(1, 6))))  # [1, 4, 9, 16, 25]
print(list(filter(even, range(1, 6))))  # [2, 4]
print([square(x) for x in range(1, 6) if even(x)])  # [4, 16]
