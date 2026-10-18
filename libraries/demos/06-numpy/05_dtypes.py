import numpy as np

samples = np.array([0.1, 0.5, -0.4], dtype=np.float32)
print(samples.dtype)
print(samples.astype(np.int16))
print(np.iinfo(np.int16).min, np.iinfo(np.int16).max)
counts = np.array([183, 126, 146], dtype=np.int64)
print(counts.dtype, counts.itemsize)
