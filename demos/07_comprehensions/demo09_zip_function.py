ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
ls3 = list(zip(ls1, ls2))
print(ls3)  # [(1, 4), (2, 5), (3, 6)]

b1, b2 = zip(*ls3)
print(b1)  # (1, 2, 3)
print(b2)  # (4, 5, 6)
