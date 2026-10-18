import numpy as np

rng = np.random.default_rng(7)
titles = np.array(["Imagine", "Yesterday", "Respect", "Toxic"])
print(rng.permutation(titles))
print(rng.choice(titles, size=2, replace=False))
print(rng.integers(0, 10, size=4))
print(rng.random(3).round(2))
print(rng.normal(0.0, 0.1, size=3).round(2))
rng.shuffle(titles)
print(titles)
