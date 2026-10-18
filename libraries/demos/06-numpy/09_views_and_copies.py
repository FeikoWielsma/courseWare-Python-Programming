from pathlib import Path

import matplotlib.image as image
import numpy as np

DATA = Path(__file__).resolve().parents[2] / "data"
photo = image.imread(DATA / "photo.png")

crop = photo[12:36, 16:48]
detached = crop.copy()
crop[0, 0] = [1.0, 0.0, 0.0]
print(photo[12, 16])
print(detached[0, 0])
print(np.shares_memory(crop, photo))
print(np.shares_memory(detached, photo))
print(np.shares_memory(photo[[0, 1]], photo))
