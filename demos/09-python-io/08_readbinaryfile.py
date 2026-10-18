with open("trilobyte.jpg", mode="rb") as photo:
    data = photo.read()
print(type(data))  # <class 'bytes'>
print(len(data))  # 49278, the size in bytes
print(data[:3].hex())  # ffd8ff, the start of every JPEG photo
