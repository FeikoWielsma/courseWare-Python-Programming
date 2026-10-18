from pathlib import Path

import matplotlib.image as image
import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
photo = image.imread(DATA / "photo.png")

print(photo[24, 32])
crop = photo[12:36, 16:48]
print(crop.shape)
flipped = photo[::-1]
print(np.array_equal(flipped[0], photo[-1]))
print(photo[:, :, 0].shape)
