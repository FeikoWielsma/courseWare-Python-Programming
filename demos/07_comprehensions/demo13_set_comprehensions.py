my_set = set(range(10))
print(my_set)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set2 = {x**2 for x in my_set}
print(my_set2)  # {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

my_set3 = {x for x in my_set if x % 2 == 0}
print(my_set3)  # {0, 8, 2, 4, 6}

my_set4 = {2**x for x in range(10)}
print(my_set4)  # {32, 1, 2, 4, 8, 64, 128, 256, 16, 512}
