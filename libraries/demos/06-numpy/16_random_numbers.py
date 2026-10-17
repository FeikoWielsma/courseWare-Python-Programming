import numpy as np

rng = np.random.default_rng()

print(np.round(rng.random(4), 3))
print(rng.integers(1, 7, size=5))
print(np.round(rng.normal(100.0, 15.0, size=4), 1))
print(np.round(rng.random((2, 3)), 2))

# Sampling from data you already have, with and without replacement.
hosts = np.array(["web01", "web02", "web03", "db01", "cache01"])
print(rng.choice(hosts, size=3, replace=False))

# shuffle rearranges in place; permutation returns a shuffled copy.
deck = np.arange(10)
print(rng.permutation(deck))
print(deck)

# The seed is what makes a demo, a test or a bug report reproducible.
print(np.random.default_rng(7).normal(size=3))
print(np.random.default_rng(7).normal(size=3))
print(np.random.default_rng(8).normal(size=3))
