def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def multiply(i, j):
    return i * j

def divide(i, j):
    return i / j

def convert_to_int_list(slist):
    ilist = []
    for x in slist:
        ilist.append(int(x))
    return ilist

def summate(ilist):
    s = 0
    for x in ilist:
        s = s + x
    return s

def average(ilist):
    s = 0
    for x in ilist:
        s = s + x
    return s / len(ilist)

def faculty(n):
    if n == 1:
        return n
    return n*faculty(n-1)
