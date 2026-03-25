# textformat.py
#
# Different examples of text formatting.

# The file stocks.csv has some CSV formatted stock market data
# "symbol",price,change,volume.   Read it into a list of dictionaries

stockdata = []
for line in open("stocks.csv"):
    fields = line.split(",")
    record = {
        'name': fields[0].strip('"'),
        'price': float(fields[1]),
        'change' : float(fields[2]),
        'volume' : int(fields[3])}
    stockdata.append(record)

# Traditional string formatting

print("Traditional string formatting:")
for s in stockdata:
    print("%(name)10s %(price)10.2f %(change)10.2f %(volume)10d" % s)

# Some new-style formatting examples
print("\nNew-style formatting:")
for s in stockdata:
    print("{name:>10s} {price:10.2f} {change:10.2f} {volume:10d}".format(**s))

print("\nNew-style formatting with dictionary lookups:")
for s in stockdata:
    print("{s[name]:>10s} {s[price]:10.2f} {s[change]:10.2f} {s[volume]:10d}".format(s=s))

