# numberlines.py

import fileinput

for line in fileinput.input(inplace=1):
    line = line.rstrip()
    num  = fileinput.lineno()
    print '%-40s # %2i' % (line, num)
