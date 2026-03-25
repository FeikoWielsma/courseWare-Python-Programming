import numpy as np

a = np.array([1, 2, 3])
print(a.min())  # 1
print(a.max())  # 3
print(a.sum())  # 6

a = np.array([(1, 2, 3), (3, 4, 5)])
print(a)
print(a.sum(axis=0))  # [4 6 8] # add elements in different rows
print(a.sum(axis=1))  # [6 12]  # add elements in different columns

a = np.array([(1, 2, 3), (3, 4, 5,)])
print(np.sqrt(a))
print(np.std(a))

# divide difference 1 3 in 10 equal parts
a = np.linspace(1, 3, 10)
print(a)

a = np.array([1, 2, 3])
print(np.exp(a))

a = np.array([1, 2, 3])
print(np.log(a))

a = np.array([1, 2, 3])
print(np.log10(a))