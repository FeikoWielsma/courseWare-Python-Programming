def intsfrom(i = 0):
    while 1:
        yield i
        i = i + 1

for x in intsfrom():
    print(x)