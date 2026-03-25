# using map and lambda
lm = list(map(lambda x: 2 * x + 1, [10, 20, 30]))
print(lm)

# using list comprehension
lc = [2 * x + 1 for x in [10, 20, 30]]
print(lc)

# using map and lambda
ls1 = list(map(lambda x: 2 * x + 1, filter(lambda x: x > 0, [10, 20, 30, -10])))
print(ls1)

# using list comprehension
ls2 = [2 * x + 1 for x in [10, 20, 30, -10] if x > 0]
print(ls2)


ls3 = [2 * x + 1 for x in [y * y for y in [10, 20, 30]]]
print(ls3)

ls4 = list(map(lambda x: 2 * x + 1, map(lambda y: y * y, [10, 20, 30])))
print(ls4)
