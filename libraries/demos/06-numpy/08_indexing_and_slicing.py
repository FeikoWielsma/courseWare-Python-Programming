import numpy as np

row = np.arange(10) * 10
print(row)
print(row[0])
print(row[-1])
print(row[2:5])
print(row[::2])
print(row[::-1])

table = np.arange(12).reshape(3, 4)
print(table)

# One index per dimension, inside one pair of brackets, separated by commas.
print(table[1, 2])
print(table[0])
print(table[:, 1])
print(table[1:, 2:])

# A whole row can be assigned in one statement.
table[0] = 999
print(table)
