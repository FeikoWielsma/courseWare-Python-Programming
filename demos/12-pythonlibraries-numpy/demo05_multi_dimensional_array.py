import numpy as np

A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)
print(A.shape)

# The Python code above returns the following results:
#[[  3.4   8.7   9.9]
# [  1.1  -7.8  -0.7]
# [  4.1  12.3   4.8]]
#2
# (3, 3)

B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(B)
print(B.ndim)
print(B.shape)

# The above Python code will return the following:
#  [121 122]]
# [[211 212]
#  [221 222]]
# [[311 312]
#  [321 322]]]
#3
# (3, 2, 2