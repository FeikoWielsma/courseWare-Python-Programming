from __future__ import generators
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
