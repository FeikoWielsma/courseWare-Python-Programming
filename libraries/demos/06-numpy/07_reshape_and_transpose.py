from pathlib import Path

import matplotlib.image as image
import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
photo = image.imread(DATA / "photo.png")

pixels = photo.reshape(-1, 3)
print(pixels.shape)
print(np.shares_memory(pixels, photo))
print(photo.transpose(1, 0, 2).shape)
print(pixels.T.shape)
