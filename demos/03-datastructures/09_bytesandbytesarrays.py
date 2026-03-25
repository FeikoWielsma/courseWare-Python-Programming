str = "ABCDE"

# arr = bytes(str, 'utf-8') # string with encoding 'utf-8'        # non mutable
arr = bytearray(str, "utf-8")  # string with encoding 'utf-8'     # mutable

print(arr)
print(arr[0])  # 65
print(arr[1])  # 66
print(arr[2])  # 67
print(arr[3])  # 68
print(arr[4])  # 69

arr[0] = 70
# arr[0] = 700  # ValueError: byte must be in range(0, 256)
arr[1] = 71
arr[2] = 72
arr[3] = 73
arr[4] = 74

str2 = arr.decode("utf-8")
print(str2)

size = 5

arr = bytes(size)
print(arr)
