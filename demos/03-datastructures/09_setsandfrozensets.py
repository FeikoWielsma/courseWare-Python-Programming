artists = {"Queen", "Queen", "ABBA"}  # Duplicate names become one member.
print(sorted(artists))  # ['ABBA', 'Queen']
requests = ["Yesterday", "Yesterday", "Respect", "Respect"]
unique = set(requests)
unique.add("Imagine")
print(sorted(unique))  # ['Imagine', 'Respect', 'Yesterday']
print("Respect" in unique)  # True

empty = set()  # {} creates an empty dictionary.
frozen = frozenset(requests)
print(sorted(frozen))  # ['Respect', 'Yesterday']

physics = {"Einstein", "Bohr", "Curie", "Fermi"}
chemistry = {"Curie", "Rutherford", "Pauling"}
print("Curie" in chemistry)  # True
print(sorted(physics | chemistry))  # union, in either set
print(sorted(physics & chemistry))  # intersection, in both
print(sorted(physics - chemistry))  # difference, in physics only
print(sorted(physics ^ chemistry))  # in one of the two, not both
