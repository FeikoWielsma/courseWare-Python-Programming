import math
import time

import numpy as np

count = 60 * 44100
start = time.perf_counter()
samples = [math.sin(2 * math.pi * 440 * i / 44100) for i in range(count)]
print(f"Python: {time.perf_counter() - start:.3f} s")
start = time.perf_counter()
times = np.arange(count) / 44100
tone = np.sin(2 * np.pi * 440 * times)
print(f"NumPy: {time.perf_counter() - start:.3f} s")
print(np.allclose(samples, tone))
