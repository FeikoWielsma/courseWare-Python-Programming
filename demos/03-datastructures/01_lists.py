li = ["abcd", 786, 2.23, "john", 70.2]

print(li)  # Prints complete list
print(li[0])  # Prints first element of the list
print(li[1:3])  # Prints elements starting from 2nd to 4th
print(li * 2)  # Prints list two times
print(li[::-1])  # Prints complete list in reverse order

li2 = []
print(li2)

li2 = li2 + li
print(li2)

print(id(li))
print(id(li2))
