with open("trilobyte.jpg", "rb") as photo:
    print(photo.read(2).hex())  # ffd8
    print(photo.tell())  # 2
    photo.seek(6)
    print(photo.read(4))  # b'JFIF'
    photo.seek(0)
    print(photo.read(2).hex())  # ffd8
