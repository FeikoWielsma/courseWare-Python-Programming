f = open(filename)
while 1:
    char = f.read(1)
    if not char:
        break
    process(char)
