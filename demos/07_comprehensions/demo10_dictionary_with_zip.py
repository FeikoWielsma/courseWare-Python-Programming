dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)  # {'a': 1, 'c': 3, 'b': 2}

dict2 = {}
dict2["a"] = 1
dict2["b"] = 2
dict2["c"] = 3
print(dict2)  # {'a': 1, 'c': 3, 'b': 2}

keys = ["a", "b", "c"]
values = [1, 2, 3]

# ls = list(zip(keys,values))
# print (ls) # [('a', 1), ('b', 2), ('c', 3)]

dict3 = {}
for k, v in zip(keys, values):
    dict3[k] = v

print(dict3)  # {'a': 1, 'b': 2, 'c': 3}

dict4 = {}
dict4 = dict(zip(keys, values))
print(dict4)
