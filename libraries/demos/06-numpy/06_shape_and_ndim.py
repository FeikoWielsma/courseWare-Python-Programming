import numpy as np

arrays = {
    "scalar": np.array(42),
    "row": np.array([1, 1, 2, 3, 5, 8, 13, 21]),
    "table": np.array([[3.4, 8.7, 9.9], [1.1, -7.8, -0.7]]),
    "cube": np.arange(12).reshape(3, 2, 2),
}

for name, array in arrays.items():
    print(f"{name:<8} ndim {array.ndim}  shape {str(array.shape):<12} size {array.size}")

table = arrays["table"]
print(table)
# Shape reads outermost first : rows, then columns. Axis 0 is the rows.
print(table.shape[0], "rows")
print(table.shape[1], "columns")
print(table.size)
