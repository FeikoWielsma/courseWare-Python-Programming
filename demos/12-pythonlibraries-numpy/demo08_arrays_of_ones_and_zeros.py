import numpy as np

# The method ones(t) takes a tuple t with
# the shape of the array and fills the array accordingly with ones.

E = np.ones((2, 3))
print(E)
F = np.ones((3, 4), dtype=int)
print(F)

# We will get the following output, if we execute the code above:
# [[ 1.  1.  1.]
# [ 1.  1.  1.]]
# [[1 1 1 1]
# [1 1 1 1]
# [1 1 1 1]]

# What we have said about the method ones() is valid for the method zeros() analogously
Z = np.zeros((2, 4))
print(Z)

# [[ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]]
