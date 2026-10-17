import sys

import numpy as np

COUNT = 1_000_000

numbers = list(range(COUNT))
# The list holds pointers; every int it points at is a separate Python object.
as_list = sys.getsizeof(numbers) + sum(sys.getsizeof(n) for n in numbers[:1000]) // 1000 * COUNT
as_array = np.arange(COUNT, dtype=np.int64).nbytes

print(f"{COUNT:,} integers")
print(f"list  : {as_list:>12,} bytes")
print(f"array : {as_array:>12,} bytes")
print(f"ratio : {as_list / as_array:.1f}x")

print(sys.getsizeof(1), "bytes for one Python int")
print(np.arange(1, dtype=np.int64).itemsize, "bytes for one array element")
