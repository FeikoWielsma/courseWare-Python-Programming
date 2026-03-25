import numpy as np

matrix = np.array(
    [[1, 4],
     [2, 0]]
)

eigvals = np.linalg.eigvals(matrix)
print(eigvals)