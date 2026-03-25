f = open(filename)
for line in f.xreadlines():
    process(line)
