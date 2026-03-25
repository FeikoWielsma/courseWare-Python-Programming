f = open(filename)
while 1:
    line = f.readline()
    if not line:
        break
    process(line)
