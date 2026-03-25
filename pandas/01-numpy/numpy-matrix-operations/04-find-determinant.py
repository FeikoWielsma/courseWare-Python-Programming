import numpy as np

matrix = np.array(
    [[1, 4],
     [2, 0]]
)

det = np.linalg.det(matrix)
print(det)