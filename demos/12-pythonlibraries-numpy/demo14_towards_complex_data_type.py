import numpy as np

dt = np.dtype([('density', np.int32)])
x = np.array([(393,), (337,), (256,)],
             dtype=dt)
print(x)
print("\nThe internal representation:")
print(repr(x))

# If we execute the code above, we can expect the following output:
# [(393,) (337,) (256,)]
# The internal representation:
# array([(393,), (337,), (256,)], 
#      dtype=[('density', '<i4')])

# We can access the content of the density column by indexing x with the key 'density'. 
# It looks like accessing a dictionary in Python:

print(x['density'])

# The above code will return the following:
# [393 337 256]