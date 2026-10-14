tup = (1, 2, 3, 4, 5, 6, 7)
print(tup[0])  # 1
print(tup[1:5])  # (2, 3, 4, 5)
print(len(tup))  # 7

li1 = ["x", 1, "y", 2]
li1[0] = "a"
li1[2] = "b"
print(li1)  # ['a', 1, 'b', 2]

tupfromlist = tuple(li1)
print(tupfromlist)  # ('a', 1, 'b', 2)
# tup[2] = 1000  # TypeError: 'tuple' object does not support item assignment
# tupfromlist[0] = "x"
# tupfromlist[2] = "y"

tup1 = (12, 34.56)
tup2 = ("abc", "xyz")
tup3 = tup1 + tup2
print(tup3)  # (12, 34.56, 'abc', 'xyz')
