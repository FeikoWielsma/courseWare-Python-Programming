text = "ABCDE"
arr = bytes(text, "utf-8")
print(arr)  # b'ABCDE'
print(arr[0])  # 65
print(arr.decode("utf-8"))  # ABCDE

mutable = bytearray(arr)
mutable[0] = 70
print(mutable)  # bytearray(b'FBCDE')
print(mutable.decode("utf-8"))  # FBCDE
