"""match anchors at the start, search looks anywhere, findall returns them all."""

import re

text = "Order 1234 shipped, order 5678 pending"

print(re.match(r"Order", text))          # matches, it is at the start
print(re.match(r"shipped", text))        # None, match only tries position zero
print(re.search(r"shipped", text))       # found, search scans the whole string

print(re.findall(r"\d+", text))          # every run of digits
print(re.findall(r"order", text, re.IGNORECASE))

print(re.fullmatch(r"[a-z]+", "hello") is not None)  # True; whole string
print(re.fullmatch(r"[a-z]+", "hello!") is not None)  # False
