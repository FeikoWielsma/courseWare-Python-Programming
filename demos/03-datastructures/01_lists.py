list1 = ["Thriller", "Imagine", "Yesterday", "Respect", "Hey Jude"]
print(list1)  # Prints complete list
print(list1[0])  # Prints first element of the list
print(list1[1:3])  # Prints the 2nd and 3rd elements
print(list1 * 2)  # Prints list two times
print(list1[::-1])  # Prints complete list in reverse order

li2 = []
print(li2)

li2 = li2 + list1
print(li2)

print(id(list1))
print(id(li2))
