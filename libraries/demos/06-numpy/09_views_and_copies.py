import numpy as np

readings = [0, 10, 20, 30, 40]
window = readings[1:4]
window[0] = 999
print("list  :", readings)

array = np.arange(10) * 10
window = array[1:4]
window[0] = 999
print("array :", array)

array = np.arange(10) * 10
window = array[1:4].copy()
window[0] = 999
print("copy  :", array)

# How to tell, without editing anything.
array = np.arange(10) * 10
view = array[1:4]
detached = array[1:4].copy()
print("view.base is array      :", view.base is array)
print("detached.base is None   :", detached.base is None)
print("view shares memory      :", np.shares_memory(view, array))
print("detached shares memory  :", np.shares_memory(detached, array))

# Fancy indexing, unlike slicing, always hands back a copy. Both look like
# square brackets, which is exactly why this catches people out.
picked = array[[1, 2, 3]]
picked[0] = 999
print(array)
