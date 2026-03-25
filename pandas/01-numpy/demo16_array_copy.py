import numpy as np

x = np.array([[42, 22, 12], [44, 53, 66]], order='F')
print(x.flags['C_CONTIGUOUS'])

y = x.copy()
x[0,0] = 1001
print(x)
print(y)

print(y.flags['C_CONTIGUOUS'])