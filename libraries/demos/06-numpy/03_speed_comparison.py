import time

import numpy as np

COUNT = 2_000_000

# Small values on purpose, so both totals stay exact and match to the digit.
left_list = [float(i % 10) for i in range(COUNT)]
right_list = [float(i % 7) for i in range(COUNT)]
left_array = np.array(left_list)
right_array = np.array(right_list)

start = time.perf_counter()
total = 0.0
for i in range(COUNT):
    total += left_list[i] * right_list[i]
slow = time.perf_counter() - start
print(f"Python loop  {slow:7.3f} s   {total:,.1f}")

start = time.perf_counter()
total = float((left_array * right_array).sum())
fast = time.perf_counter() - start
print(f"NumPy arrays {fast:7.3f} s   {total:,.1f}")

print(f"{slow / fast:.0f}x faster")
