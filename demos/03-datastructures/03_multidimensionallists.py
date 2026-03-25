multilist = [["a", "b", "c"], [1, 2, 3, 4]]

# first row
print(multilist[0][0])
print(multilist[0][1])
print(multilist[0][2])

# second row
print(multilist[1][0])
print(multilist[1][1])
print(multilist[1][2])
print(multilist[1][3])

# print (multilist[1][4]) # IndexError: list index out of range

del multilist[0][2]
print(multilist)  # [['a', 'b'], [1, 2, 3, 4]]
multilist.remove(["a", "b"])
print(multilist)  # [[1, 2, 3, 4]]
