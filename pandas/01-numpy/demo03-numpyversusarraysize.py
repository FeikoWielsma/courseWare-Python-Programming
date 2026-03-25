import numpy as np

import time
import sys

S = range(1000)
print(sys.getsizeof(6) * len(S))

D = np.arange(1000)         # dtype=np.int8
print(D.size * D.itemsize)