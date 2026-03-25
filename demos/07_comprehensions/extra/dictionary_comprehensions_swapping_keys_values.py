my_dict = {"a": 1, "b": 2, "c": 3}
my_dict2 = {value: key for key, value in my_dict.items()}

print(my_dict2)

# Works if the values of the dictionary are immutable, like strings or tuples
# If you try this with a dictionary that contains lists, it will fail

some_dict = {"a": [1, 2, 3], "b": 4, "c": 5}
some_dict2 = {value: key for key, value in some_dict.items()}
