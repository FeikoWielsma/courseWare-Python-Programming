tup1 = ("physics", "chemistry", "biology", "computer science")
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"  # not recommended
tup4 = ()                  # empty tuple
tup5 = (50,)               # single element tuple
print(tup2, tup3, tup4, tup5)

t = ()
print(t)
print(tuple())

print(tup1)
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])

singleton = ("hello",)  # <-- note trailing comma

print(len(singleton))  # 1
print(singleton)  # ('hello',)
