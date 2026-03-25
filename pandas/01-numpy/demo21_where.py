import numpy as np

a = np.array(['apple', 'orange', 'apple', 'banana'])

arr_index = np.where(a == 'apple')

print(arr_index)

print(a[arr_index])