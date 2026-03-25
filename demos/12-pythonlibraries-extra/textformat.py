# textformat.py
#
# Different examples of text formatting illustrated by the output of
# table in different formats.

# The file stocks.csv has some CSV formatted stock market data
# "symbol",price,change,volume.   Read it into a list of tuples

stockdata = []
for line in open("stocks.csv"):
    fields = line.split(",")
    record = (fields[0].strip('"'),float(fields[1]),float(fields[2]),int(fields[3]))
    stockdata.append(record)

# Traditional string formatting

print("Traditional string formatting:")
for s in stockdata:
    print("%10s %10.2f %10.2f %10d" % s)

# Some new-style formatting examples
print("\nNew-style formatting:")
for s in stockdata:
    print("{0:10s} {1:10.2f} {2:10.2f} {3:10d}".format(*s))

print("\nNew-style formatting with omitted fields")
for s in stockdata:
    print("{:10s} {:10.2f} {:10.2f} {:10d}".format(*s))

print("\nNew-style formatting with alignment:")
for s in stockdata:
    print("{0:>10s} {1:10.2f} {2:10.2f} {3:10d}".format(*s))

print("\nNew-style formatting with indexing")
for s in stockdata:
    print("{0[0]:>10s} {0[1]:10.2f} {0[2]:10.2f} {0[3]:10d}".format(s))

WIDTH = 18
print("\nNew-style formatting with customizable width")
for s in stockdata:
    print("{0:{width}s} {1:{width}.2f} {2:{width}.2f} {3:{width}d}".format(*s,width=WIDTH))

