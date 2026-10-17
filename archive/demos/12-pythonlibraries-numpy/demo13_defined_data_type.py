import numpy as np

i16 = np.dtype(np.int16)
print(i16)

lst = [[3.4, 8.7, 9.9], [1.1, -7.8, -0.7], [4.1, 12.3, 4.8]]
A = np.array(lst, dtype=i16)
print(A)

# We can expect the following result, if we execute the code above:
# int16
# [[ 3  8  9]
# [ 1 -7  0]
# [ 4 12  4]]
