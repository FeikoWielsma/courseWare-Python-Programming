def square(x):
    return x * x


def even(x):
    return x % 2 == 0


some_list = list(map(square, range(10, 20)))
print(some_list)

some_list = list(filter(even, range(10, 20)))
print(some_list)

some_list = list(map(square, filter(even, range(10, 20))))
print(some_list)
