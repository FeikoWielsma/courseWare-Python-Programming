from functools import reduce


def add (i, j):
    z = i + j
    return z

def subtract (i, j):
    z = i - j
    return z

def multiply (i, j):
    z = i * j
    return z

def divide (i, j):
    z = i / j
    return z

# def convertointlist(slist):
#     ilist = []
#     for x in slist :
#         x = int(x)
#         ilist.append(x)
#     return ilist

def convertointlist(slist):
    return [int(x) for x in slist]

# def summate(ilist):
#     s = 0
#     for x in ilist :
#         s = s + x
#     return s

def summate(ilist):
    return reduce((lambda x, y: x + y), ilist)

# def average(ilist):
#     s = 0
#     for x in ilist :
#         s = s + x
#     av = s / len(ilist)
#     return av

def average(ilist):
    return reduce((lambda x, y: x + y), ilist)/len(ilist)

def faculty(n):
    if (n == 1):
        return n
    return n*faculty(n-1)
