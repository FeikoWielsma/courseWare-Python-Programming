# textformat.py
#
# Different examples of text formatting.

# The file stocks.csv has some CSV formatted stock market data
# "symbol",price,change,volume.   Read it into a list of dictionaries

from collections import namedtuple

StockData = namedtuple("StockData", ["name", "price", "change", "volume"])

stockdata = []
for line in open("stocks.csv"):
    fields = line.split(",")
    record = StockData(
        fields[0].strip('"'), float(fields[1]), float(fields[2]), int(fields[3])
    )
    stockdata.append(record)

# Traditional string formatting

print("Traditional string formatting:")
for s in stockdata:
    print("%10s %10.2f %10.2f %10d" % (s.name, s.price, s.change, s.volume))

# Some new-style formatting examples
print("\n_new-style formatting:")
for s in stockdata:
    print("{s.name:>10s} {s.price:10.2f} {s.change:10.2f} {s.volume:10d}".format(s=s))
