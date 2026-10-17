import numpy as np

print(np.array([3, 1, 4, 1, 5]))
print(np.array([[1, 2, 3], [4, 5, 6]]))

print(np.arange(0, 10, 2))
# linspace asks the other question : how many points, evenly spaced?
print(np.linspace(0.0, 1.0, 5))

print(np.zeros((2, 4)))
print(np.ones(3, dtype=int))
print(np.full(1000, 7.5) * 2)

# A shape is a tuple, so a one-dimensional shape needs no tuple at all.
print(np.zeros(3).shape)
print(np.zeros((3, 1)).shape)
