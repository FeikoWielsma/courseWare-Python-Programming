from struct import pack, unpack

payload = pack("<iii", 1, 2, 3)
fw = open("numbers.bin", mode="wb")
fw.write(payload)
fw.close()

fr = open("numbers.bin", mode="rb")
print(unpack("<iii", fr.read()))  # (1, 2, 3)
fr.close()
