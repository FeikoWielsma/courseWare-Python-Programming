from pathlib import Path

import matplotlib.image as image
import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
photo = image.imread(DATA / "photo.png")

factors = np.array([1.1, 1.0, 0.9])
corrected = np.clip(photo * factors, 0.0, 1.0)
print(photo.shape, factors.shape, corrected.shape)
print(np.broadcast_shapes((48, 64, 3), (3,)))
print(np.broadcast_shapes((3, 1), (4,)))
