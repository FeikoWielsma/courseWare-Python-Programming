# Initialize dict from keys
dict9 = dict.fromkeys(["a", "b", "c"], 0)
print(dict9)  # {'a': 0, 'c': 0, 'b': 0}

# Can use dictionary comprehension to do the same thing
dict10 = {k: 0 for k in ["a", "b", "c"]}
print(dict10)  # {'a': 0, 'c': 0, 'b': 0}

dict11 = dict.fromkeys("dictionary")
print(
    dict11
)  # {'d': None, 'o': None, 'i': None, 't': None, 'a': None, 'c': None, 'y': None, 'n': None, 'r': None}

dict12 = {k: None for k in "dictionary"}
print(
    dict12
)  # {'t': None, 'y': None, 'c': None, 'd': None, 'i': None, 'r': None, 'o': None, 'n': None, 'a': None}
