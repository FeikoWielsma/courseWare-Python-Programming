import numpy as np

print(np.array([1, 2, 3]).dtype)
print(np.array([1.0, 2, 3]).dtype)
print(np.array([True, False]).dtype)
print(np.array(["ab", "cde"]).dtype)

# Ask for a type and you get it, whether or not the values survive.
whole = np.array([1.7, 2.9, -3.4], dtype=np.int32)
print(whole)

# An assignment into an array converts to the array's dtype, silently.
counts = np.zeros(4, dtype=np.int64)
counts[0] = 9.99
print(counts)

# A fixed width is a real limit, and NumPy enforces it rather than growing.
print(np.iinfo(np.int8).min, np.iinfo(np.int8).max)
small = np.zeros(2, dtype=np.int8)
try:
    small[0] = 300
except OverflowError as error:
    print(error)

print(whole.astype(np.float64).dtype)
