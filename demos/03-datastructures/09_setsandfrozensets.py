artists = {"Nova", "Nova", "Echo"}  # Duplicate names become one member.
print(sorted(artists))  # ['Echo', 'Nova']
requests = ["Echo", "Echo", "Pulse", "Pulse"]
unique = set(requests)
unique.add("Orbit")
print(sorted(unique))  # ['Echo', 'Orbit', 'Pulse']
print("Pulse" in unique)  # True

empty = set()  # {} creates an empty dictionary.
frozen = frozenset(requests)
print(sorted(frozen))  # ['Echo', 'Pulse']

day_one = {"Nova", "Echo", "Pulse", "Orbit"}
day_two = {"Pulse", "Muse", "Vega"}
print("Pulse" in day_two)  # True
print(sorted(day_one | day_two))  # union, in either set
print(sorted(day_one & day_two))  # intersection, in both
print(sorted(day_one - day_two))  # difference, in day_one only
print(sorted(day_one ^ day_two))  # in one of the two, not both
