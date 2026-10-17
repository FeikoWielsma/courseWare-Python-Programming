import numpy as np

# Response times in milliseconds, from one minute of probes.
latency = np.array([12.1, 9.8, 14.0, 210.5, 11.2, 13.7, 480.0, 10.9, 12.4, 195.3])
SLOW_MS = 100.0

mask = latency > SLOW_MS
print(mask)

# Indexing with the mask keeps the elements where it is True.
print(latency[mask])
print(mask.sum())
print(mask.any(), mask.all())

# Conditions combine with & and |, and each one needs its own brackets.
print(latency[(latency > 12.0) & (latency < 100)])

# The mask also works on the left of an assignment.
clipped = latency.copy()
clipped[clipped > SLOW_MS] = SLOW_MS
print(clipped)

# nonzero turns the mask back into positions, which is often what you want.
print(np.nonzero(mask)[0])
