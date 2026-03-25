# Controlling Iteration Order:

# There are times when it is important to visit the elements of an array in a
# specific order, irrespective of the layout of the elements in memory. The nditer
# object provides an order parameter to control this aspect of iteration.
# The default, having the behavior described above, is order=’K’ to keep the existing order.
# This can be overridden with order=’C’ for C order and order=’F’ for Fortran order.

# Python program for iterating over array # using particular order

import numpy as np

# creating an array using arrange method
a = np.arange(12)

# shape array with 3 rows and 4 columns
a = a.reshape(3, 4)

print('Original array is:')
print(a)


print('Iteration an array in C-style order:')
for x in np.nditer(a, order='C'):
    print(x, end=' ')

print()

print('Iteration an array in F-style order:')
for x in np.nditer(a, order='F'):
    print(x, end=' ')