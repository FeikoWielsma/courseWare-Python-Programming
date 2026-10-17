import numpy as np

# The rule : line the shapes up from the right. Dimensions are compatible when
# they are equal, or when one of them is 1, which then stretches.
for left, right in [((3, 4), ()), ((3, 4), (4,)), ((3, 1), (4,)), ((3, 4), (3,))]:
    try:
        outcome = str(np.broadcast_shapes(left, right))
    except ValueError:
        outcome = "refused, the shapes do not line up"
    print(f"{str(left):<8} with {str(right):<8} -> {outcome}")

# Three servers, four hourly readings each.
load = np.array([[10.0, 20.0, 30.0, 40.0], [5.0, 6.0, 7.0, 8.0], [50.0, 55.0, 60.0, 65.0]])
print(load)

# A (3, 1) column of baselines subtracts one value from each whole row.
baseline = np.array([10.0, 5.0, 50.0]).reshape(3, 1)
print(load - baseline)

# A (4,) row of weights applies one value to each whole column.
print(load * np.array([1.0, 1.0, 2.0, 2.0]))
