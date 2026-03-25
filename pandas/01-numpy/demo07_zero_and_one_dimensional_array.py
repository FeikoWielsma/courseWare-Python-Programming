import numpy as np

x = np.array(42)
print(type(x))
print(np.ndim(x))

#The above code will return the following result:
#<class 'numpy.ndarray'>
#0

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
V = np.array([3.4, 6.9, 99.8, 12.8])
print(F.dtype)
print(V.dtype)
print(np.ndim(F))
print(np.ndim(V))

# Executing the Python above code will return the following:
# int64
# float64
# 1
# 1