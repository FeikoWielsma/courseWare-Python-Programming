# The duplicates in the first set literal are the point: a set drops them.

s1 = {1, 1, 2, 2}
print(s1)  # {1, 2}
numbers = [3, 3, 4, 4]
s2 = set(numbers)
print(s2)  # {3, 4}
s2.add(5)
print(s2)  # {3, 4, 5}
print(4 in s2)  # True, a fast membership test

empty = set()  # {} would be an empty dictionary
print(len(empty))  # 0

frozen = frozenset(numbers)
print(frozen)  # frozenset({3, 4})
# frozen.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

day_one = {"Nova", "Echo", "Pulse", "Orbit"}
day_two = {"Pulse", "Muse", "Vega"}
print("Pulse" in day_two)  # True
print(sorted(day_one | day_two))  # union, in either set
print(sorted(day_one & day_two))  # intersection, in both
print(sorted(day_one - day_two))  # difference, in day_one only
print(sorted(day_one ^ day_two))  # in one of the two, not both
