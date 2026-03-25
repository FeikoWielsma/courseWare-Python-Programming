import numpy as np

A = np.array([[3.4, 8.7, 9.9],
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
print(A)
print(A.ndim)
print(A.shape)

# The Python code above returns the following results:
#[[  3.4   8.7   9.9]
# [  1.1  -7.8  -0.7]
# [  4.1  12.3   4.8]]
# 2
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
# 3
# (3, 2, 2)

# The function "shape" returns the shape of an array. The shape is a
# tuple of integers. These numbers denote the lengths of the corresponding
# array dimension.

x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])
print(np.shape(x))