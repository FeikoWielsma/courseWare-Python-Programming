import pandas as pd

# The index is the left-hand column. It is not a row number : it is a label,
# and it travels with the values through every operation.
free_gb = pd.Series(
    [55.5, 48.8, 550.0, 880.0], index=["web01", "web02", "db01", "log01"], name="free_gb"
)
print(free_gb)

print(free_gb["db01"])

print(list(free_gb.index))
# print(free_gb.to_numpy())
# print(free_gb.dtype)

# # Arithmetic applies to every element at once, and so does a comparison.
# print(free_gb / 1024)
# print(free_gb > 100)
