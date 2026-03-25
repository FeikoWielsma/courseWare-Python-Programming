import numpy as np

# We have a list with values, e.g. temperatures in Celsius:
cvalues = [25.3, 24.8, 26.9, 23.9]

# We will turn this into a one-dimensional 01-numpy array:
C = np.array(cvalues)
print(C)

# Let's assume, we want to turn the values into degrees Fahrenheit. 
# This is very easy to accomplish with a 01-numpy array.
# The solution to our problem can be achieved by simple scalar multiplication:
print(C * 9 / 5 + 32)

# Compared to this, the solution for our Python list is extremely awkward:
fvalues = [ x*9/5 + 32 for x in cvalues] 
print(fvalues)