import numpy as np

ca = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(ca[0][0])
# print(ca[0][1])
# print(ca[0][2])
# print(ca[0][3])
# print(ca[0][4])
#
# print(ca[1][0])
# print(ca[1][1])
# print(ca[1][2])
# print(ca[1][3])
# print(ca[1][4])

# print(ca[0])
# print(ca[0].shape)
# print(ca[0].ndim)
# print(ca[1])
# print(ca[1].shape)
# print(ca[1].ndim)

print(len(ca))
print(len(ca[0]))
print(len(ca[1]))

for i in range(len(ca)):
    for j in range(len(ca[i])):
        print(ca[i][j], end = ' ')

# creating an array using arrange method
a = np.arange(12)
a = a.reshape(3, 4)

print()
print('Original array is:')
print(a)
print()

# iterating  an array
for x in np.nditer(a):
    print(x, end=' ')