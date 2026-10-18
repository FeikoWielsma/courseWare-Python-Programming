from pathlib import Path

import matplotlib.image as image

DATA = Path(__file__).resolve().parents[2] / "data"
photo = image.imread(DATA / "photo.png")

print(photo.shape)
print(photo.ndim)
print(photo.size)
print(photo[0, 0].shape)
