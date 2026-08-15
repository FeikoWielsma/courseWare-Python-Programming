from functools import reduce


def add (i, j):
    return i + j

def subtract (i, j):
    return i - j

def multiply (i, j):
    return i * j

def divide (i, j):
    return i / j

# def convert_to_int_list(slist):
#     ilist = []
#     for x in slist :
#         x = int(x)
#         ilist.append(x)
#     return ilist

def convert_to_int_list(slist):
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
