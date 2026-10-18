import numpy as np

times = np.arange(8) / 8000
samples = np.sin(2 * np.pi * 440 * times)
print(samples.round(3))
print(samples * 0.5)
