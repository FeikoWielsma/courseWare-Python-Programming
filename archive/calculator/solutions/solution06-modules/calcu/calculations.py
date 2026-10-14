def add(i: float, j: float) -> float:
    return i + j

def subtract(i: float, j: float) -> float:
    return i - j

def multiply(i: float, j: float) -> float:
    return i * j

def divide(i: float, j: float) -> float:
    return i / j

def convert_to_int_list(slist: list[str]) -> list[int]:
    ilist = []
    for x in slist :
        ilist.append(int(x))
    return ilist

def summate(ilist: list[int]) -> int:
    s = 0
    for x in ilist:
        s = s + x
    return s

def average(ilist: list[int]) -> float:
    s = 0
    for x in ilist:
        s = s + x
    return s / len(ilist)

def faculty(n: int) -> int:
    if n == 1:
        return n
    return n*faculty(n-1)
