# textop.py
#
# A program that reads a large collection of text into memory 
# and performs various operations on it.   This should work in both
# Python 2 and Python 3.  Use it for a performance comparison.

NSAMPLES = 10
from timethis import timethis
import sys

# For Python 2, map range to xrange
try:
    range = xrange
except NameError:
    pass

# Read an Apache log file into memory and replicate it to make a large sample.
# The result should be a string with about 6 million characters in it
logdata = open("access-log","rt").read()*10

# Test 1: Memory use
print("Size %d bytes" % sys.getsizeof(logdata))

# Test 2: Finding all lines using find() and slicing
with timethis("find lines"):
    index = 0
    while index < len(logdata):
        nextindex = logdata.find("\n",index)
        line = logdata[index:nextindex]
        index = nextindex+1

# Test 3 : Split into lines
with timethis("line splitting"):
    lines = logdata.splitlines()

# Test 4 : Splitting on whitespace
with timethis("whitespace splitting"):
    fields = logdata.split()

# Test 5 : Regex pattern matching.  
import re
ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
with timethis("regex pattern matching"):
    unique_ips = set()
    for m in ip_pattern.finditer(logdata):
        unique_ips.add(m.group())

# Test 6 : Iterate by characters
with timethis("iterate by character"):
    for c in logdata:
        pass

# Test 7 : Replace text
with timethis("Replace characters"):
    s = logdata.replace(" ",":")



