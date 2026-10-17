import numpy as np

readings = np.arange(12)
print(readings)

# The element count has to survive : 12 elements make 3 x 4 or 4 x 3.
table = readings.reshape(3, 4)
print(table)

# -1 means "work the remaining dimension out for me".
print(readings.reshape(-1, 2).shape)

print(table.T)
print(table.T.shape)

# Neither call copied anything. Both are windows onto the same 12 numbers.
print(np.shares_memory(table, readings))
print(np.shares_memory(table.T, readings))

readings[0] = 99
print(table[0, 0])
