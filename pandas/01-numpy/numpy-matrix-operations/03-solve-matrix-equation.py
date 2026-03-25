import numpy as np

A = np.array(
    [[1, 4],
     [2, 0]]
)

B = np.array(
    [[-1, 2],
     [1, -2]]
)

X = np.linalg.solve(A, B)
print(X)