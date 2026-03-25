def add(i, j):
    z = i + j
    return z

def subtract(i, j):
    z = i - j
    return z

def multiply(i, j):
    z = i * j
    return z

def divide(i, j):
    z = i / j
    return z

def convertointlist(slist):
    ilist = []
    for x in slist:
        x = int(x)
        ilist.append(x)
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
    av = s / len(ilist)
    return av

def faculty(n):
    if n == 1:
        return n
    return n*faculty(n-1) 
