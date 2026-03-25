# structwrite.py
#
# An example of writing a binary-packed data structure

from timethis import timethis
import struct
from random import random

# Create a million random (x,y) points
points = [(random(), random()) for n in range(1000000)]

# Write out to a file using write() and struct.pack()
with timethis("Writing many small structs"):
    f = open("pts1.bin", "wb")
    f.write(struct.pack("I", len(points)))
    for p in points:
        f.write(struct.pack("ff", *p))
    f.close()

# Pack a bytearray and write it all at once
with timethis("Packing a bytearray and writing"):
    out = bytearray()
    out.extend(struct.pack("I", len(points)))
    for p in points:
        out.extend(struct.pack("ff", *p))
    f = open("pts2.bin", "wb")
    f.write(out)
    f.close()
