from pathlib import Path

import matplotlib.image as image
import numpy as np

# Fictional counts for three days and four hours.

plays = np.array([[1, 2, 3, 4], [2, 0, 1, 3], [0, 1, 2, 1]])
print(plays.sum())
print(plays.sum(axis=0))
print(plays.sum(axis=1))
print(plays.sum(axis=1, keepdims=True).shape)



photo = image.imread(Path(__file__).resolve().parents[2] / "data" / "photo.png")
brightness_per_row = photo.mean(axis=(1, 2))
print(brightness_per_row.shape)
