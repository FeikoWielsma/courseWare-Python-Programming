# Logical
sunny = True
warm = False
print(sunny and warm)  # False
print(sunny or warm)  # True
print(not sunny)  # False

name = ""
print(name or "anonymous")  # anonymous, `or` returns the first truthy operand
print(name and "anonymous")  # an empty line, `and` returns the first falsy operand

age = 17
print("adult" if age >= 18 else "minor")  # minor

# Membership
s = "ABC"
print("B" in s)  # True
print("Z" not in s)  # True
primes = [2, 3, 5, 7]
print(4 in primes)  # False

# Identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c)  # True, equal values
print(a is c)  # False, two different lists
print(a is b)  # True, two names for one list
