li = ["physics", "chemistry", "biology", "computer science"]

print("Value available at index 2 : ")
print(li[2])
li[2] = "mathematics"
print("New value available at index 2 : ")
print(li[2])

print(li)
del li[2]
print("After deleting value at index 2 : ")
print(li)  # ['physics', 'chemistry', 'computer science']

li.remove("physics")
print("After deleting value 'physics' ")
print(li)  # ['chemistry', 'computer science']

li2 = [1, 2, 3]
li2.append(4)
li2.append(5)
print(li2)  # [1, 2, 3, 4, 5]

li2.insert(0, 99)
print(li2)  # [99, 1, 2, 3, 4, 5]

li2.extend([33, 44, 55])
print(li2)  # [99, 1, 2, 3, 4, 5, 33, 44, 55]

print(li2[::-2])  # [55, 33, 4, 2, 99]
del li2
# li2.append(100)
