import numpy as np

a = np.array([(8, 9, 10), (11, 12, 13)])
print(a)
print(a.shape)

# a = a.transpose()
# print(a)

# b = a.T
# print(b)
# print(b.shape)

a = a.reshape(3, 2)
print(a)
print(a.shape)

a = a.reshape(2, 3)
print(a)
print(a.shape)

a = a.reshape(1, 6)
print(a)
print(a.shape)

a = a.reshape(6, 1)
print(a)
print(a.shape)

