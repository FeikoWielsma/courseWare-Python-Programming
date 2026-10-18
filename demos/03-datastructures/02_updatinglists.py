playlist = ["Thriller", "Imagine", "Yesterday", "Hey Jude"]

print("Value available at index 2 : ")
print(playlist[2])
playlist[2] = "Jolene"
print("New value available at index 2 : ")
print(playlist[2])

print(playlist)
del playlist[2]
print("After deleting value at index 2 : ")
print(playlist)  # ['Thriller', 'Imagine', 'Hey Jude']

playlist.remove("Thriller")
print("After deleting value 'Thriller' ")
print(playlist)  # ['Imagine', 'Hey Jude']

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
