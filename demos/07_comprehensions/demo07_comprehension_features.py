list_d = [("a", 1), ("b", 2), ("c", 7)]
list_e = [n * 3 for (x, n) in list_d]
print(list_e)  # [3, 6, 21]


def subtract(a, b):
    return a - b


oplist = [(6, 3), (1, 7), (5, 5)]
list_f = [subtract(y, x) for (x, y) in oplist]
print(list_f)  # ([-3, 6, 0])

list_a = ["A", "B"]
list_b = [1, 2]

list_c = []
list_c = [(x, y) for x in list_a for y in list_b]
print(list_c)
# [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
