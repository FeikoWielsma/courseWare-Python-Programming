a = b = c = 10
print(a, b, c)
print(id(a), id(b), id(c))

a = 11
print(a, b, c)
print(id(a), id(b), id(c))

d = 10
print(d)
print(id(d))

a, b, c = 1, 2, "pipo"
print(a, b, c)
