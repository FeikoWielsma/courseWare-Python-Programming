import math
import sys

import numpy as np

count = 60 * 44100
samples = [math.sin(2 * math.pi * 440 * i / 44100) for i in range(count)]
tone = np.array(samples)
list_bytes = sys.getsizeof(samples) + sum(sys.getsizeof(x) for x in samples)
print(f"list: {list_bytes:,} bytes")
print(f"array: {tone.nbytes:,} bytes")
