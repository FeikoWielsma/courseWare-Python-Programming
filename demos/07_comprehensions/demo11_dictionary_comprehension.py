keys = ["a", "b", "c"]
values = [1, 2, 3]

dict5 = {k: v for (k, v) in zip(keys, values)}
print(dict5)  # {'a': 1, 'b': 2, 'c': 3}

# constructor function
dict6 = dict(zip(keys, values))
print(dict6)  # {'a': 1, 'b': 2, 'c': 3}

dict7 = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(dict7)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict8 = {x.upper(): x * 3 for x in "abcd"}
print(dict8)  # {'A': 'aaa', 'B': 'bbb', 'C': 'ccc', 'D': 'ddd'}
