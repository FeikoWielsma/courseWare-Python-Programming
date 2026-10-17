import numpy as np

SERVERS = ["web01", "web02", "db01"]

# Deliberately unrealistic values, chosen so every total can be checked by eye.
load = np.array([[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]])
print(load)

# No axis : every dimension goes, and a single number comes back.
print(load.sum())

# axis=0 is the row dimension, so the rows go and the columns survive.
# Reading down each column : 1+10+100, 2+20+200, and so on.
print(load.sum(axis=0), load.sum(axis=0).shape)

# axis=1 is the column dimension, so the columns go and the rows survive.
# Reading along each row : 1+2+3+4, 10+20+30+40, 100+200+300+400.
print(load.sum(axis=1), load.sum(axis=1).shape)

print(SERVERS[int(np.argmax(load.sum(axis=1)))])
print(int(np.argmax(load.sum(axis=0))))

# keepdims leaves the collapsed dimension in place, as size 1, which is exactly
# the shape broadcasting needs to divide each row by its own total.
totals = load.sum(axis=1, keepdims=True)
print(totals.shape)
print(np.round(load / totals, 2))
