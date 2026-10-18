title = "Jóga"
data = title.encode("utf-8")
print(data)  # b'J\xc3\xb3ga'
print(len(title), len(data))  # 4 5
print(data[0])  # 74
print(data.decode("utf-8"))  # Jóga

mutable = bytearray(data)
mutable[0] = 89
print(mutable)  # bytearray(b'Y\xc3\xb3ga')
print(mutable.decode("utf-8"))  # Yóga
