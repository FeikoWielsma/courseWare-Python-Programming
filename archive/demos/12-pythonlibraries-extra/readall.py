# readall.py
#
# Read a text file all at once

from timethis import timethis

with timethis("Read a text file"):
    data = open("big.txt").read()

with timethis("Read a binary file"):
    data = open("big.txt", "rb").read()
