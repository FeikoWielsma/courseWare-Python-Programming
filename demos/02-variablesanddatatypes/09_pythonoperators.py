# Arithmetic
print(7 / 2)  # 3.5, true division always gives a float
print(7 // 2)  # 3, floor division drops the fraction
print(7 % 2)  # 1, the remainder
print(2**10)  # 1024, exponentiation

# Assignment
count = 10
count += 1
count *= 2
print(count)  # 22

# Comparison
i = 10
j = 11
print(i > j)  # False
print(i != j)  # True
print(0 < i < 20)  # True, comparisons chain
print("apple" < "banana")  # True, strings compare letter by letter

# Precedence
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
print(2**3**2)  # 512, ** groups from the right
