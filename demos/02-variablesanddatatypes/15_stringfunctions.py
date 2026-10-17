name = "  Marie Curie  "
print(repr(name.strip()))  # 'Marie Curie'

name = name.strip()
print(name.lower())  # marie curie
print(name.upper())  # MARIE CURIE
print(len(name))  # 11

words = name.split()
print(words)  # ['Marie', 'Curie']
print("-".join(words))  # Marie-Curie

print(name.count("i"))  # 2
print(name.startswith("Mar"))  # True
print(name.isalpha())  # False, the space is not a letter
print("étage".isascii())  # False, é is not plain ASCII
print(name.replace("Marie", "Pierre"))  # Pierre Curie
print(name.find("Curie"))  # 6
print(name.find("Bohr"))  # -1, not found
print("one\ntwo".splitlines())  # ['one', 'two']
