fr = open("trilobyte.jpg", mode="rb")
data = fr.read(3)
print(type(data))  # <class 'bytes'>
print(data.hex())  # ffd8ff
fr.close()
