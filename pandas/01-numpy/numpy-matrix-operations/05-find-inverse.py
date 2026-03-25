import numpy as np

matrix = np.array(
    [[1, 4],
     [2, 0]]
)

inverse = np.linalg.inv(matrix)
print(inverse)