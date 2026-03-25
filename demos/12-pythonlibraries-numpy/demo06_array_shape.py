import numpy as np

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