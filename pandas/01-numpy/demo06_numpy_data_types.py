import numpy as np

i8 = np.dtype(np.int8)
print(i8)
print(i8.itemsize)  # gives size in bytes

i16 = np.dtype(np.int16)
print(i16)
print(i16.itemsize)  # gives size in bytes

i32 = np.dtype(np.int32)
print(i32)
print(i32.itemsize)  # gives size in bytes

i64 = np.dtype(np.int64)
print(i64)
print(i64.itemsize)  # gives size in bytes

f16 = np.dtype(np.float16)
print(f16)
print(f16.itemsize)  # gives size in bytes

f32 = np.dtype(np.float32)
print(f32)
print(f32.itemsize)  # gives size in bytes

f64 = np.dtype(np.float64)
print(f64)
print(f64.itemsize)  # gives size in bytes

fo = np.dtype(np.object)
print(fo)
print(fo.itemsize)  # gives size in bytes

lst = [[3.4, 8.7, 9.9],
        [1.1, -7.8, -0.7],
        [4.1, 12.3, 4.8]]
A = np.array(lst, dtype=i16)
print(A)

#We can expect the following result, if we execute the code above:
#int16
#[[ 3  8  9]
# [ 1 -7  0]
# [ 4 12  4]]

