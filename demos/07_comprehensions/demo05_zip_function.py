keys = ["a", "b", "c"]
values = [1, 2, 3]
pairs = list(zip(keys, values))
print(pairs)  # [('a', 1), ('b', 2), ('c', 3)]
checked = list(zip(keys, values, strict=True))  # the lengths match, so no error
print(checked)  # [('a', 1), ('b', 2), ('c', 3)]
