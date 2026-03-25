import numpy as np

matrix = np.array(
    [[1, 4],
     [2, 0]]
)

eigvec = np.linalg.eigh(matrix)
print(eigvec)