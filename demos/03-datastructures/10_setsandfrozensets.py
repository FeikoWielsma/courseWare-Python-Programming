basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
print("orange" in basket)  # True, fast membership testing

print("crabgrass" in basket)  # False

s1 = {1, 1, 2, 2}
print(s1)  # {1, 2}
s2 = set([3, 3, 4, 4])
# s2 = frozenset([3,3,4,4])
# s3 = set(7,7,8,8)   # TypeError: set expected at most 1 arguments, got 4
print(s2)  # {3, 4}
s2.add(
    5
)  # Gives error for frozenset, AttributeError: 'frozenset' object has no attribute 'add'
print(s2)  # {3, 4, 5}

# Demonstrate set operations on unique letters from two words

a = set("abracadabra")
b = set("alacazam")
print(a)  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
print(a - b)  # letters in a but not in b
# {'r', 'd', 'b'}
print(a | b)  # letters in either a or b
#'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)  # letters in both a and b
# {'a', 'c'}
print(a ^ b)  # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}
