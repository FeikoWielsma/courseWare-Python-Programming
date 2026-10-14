from struct import pack, unpack

# writing binary data file
fw = open("binaryfile04.txt", mode="wb")
print(fw.mode)
print(fw.name)

nr1 = 1
nr2 = 2
result = nr1 + nr2
buffer = pack("iii", nr1, nr2, result)
fw.write(buffer)
fw.close()

# reading binary data file
fr = open("binaryfile04.txt", mode="rb")
buffer = fr.read()
data = unpack("iii", buffer)

print(type(data))
num1, num2, res = data
print(num1)
print(num2)
print(res)

fr.close()
