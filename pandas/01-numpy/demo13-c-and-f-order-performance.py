import numpy as np
import time

a = np.random.standard_normal((10000, 10000))
print(a.shape)
c = np.array(a, order='C')
f = np.array(a, order='F')

start = time.time()
c.sum(axis=0)
print(f"C order axis = 0 {((time.time() - start) * 100000)}")

start = time.time()
c.sum(axis=1)
print(f"C order axis = 1 {((time.time() - start) * 100000)}")

start = time.time()
f.sum(axis=0)
print(f"F order axis = 0 {((time.time() - start) * 100000)}")

start = time.time()
f.sum(axis=1)
print(f"F order axis = 1 {((time.time() - start) * 100000)}")