with open("positions.bin", "wb") as fw:
    fw.write(b"ABCDE")

with open("positions.bin", "rb") as fr:
    print(fr.read(2))  # b'AB'
    print(fr.tell())  # 2
    fr.seek(0)
    print(fr.read(2))  # b'AB'
