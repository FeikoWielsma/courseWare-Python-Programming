def benchmark(func):
    """ A decorator that prints the time a function takes to execute. """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print (func.__name__, time.clock()-t)
        return res
    return wrapper

def logging(func):
    """ A decorator that logs the activity of the script.
        (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print (func.__name__, args, kwargs)
        return res
    return wrapper

def counter(func):
    """ A decorator that counts and prints the number of times a function has been executed"""
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print (f"{func.__name__} has been used: {wrapper.count}x")
        return res
    wrapper.count = 0
    return wrapper

@counter
@logging
@benchmark
def add (i, j):
    z = i + j
    return z

@counter
@logging
@benchmark
def subtract (i, j):
    z = i - j
    return z

@counter
@logging
@benchmark
def multiply (i, j):
    z = i * j
    return z

@counter
@logging
@benchmark
def divide (i, j):
    z = i / j
    return z

@counter
@logging
@benchmark
def convert_to_int_list(slist):
    ilist = []
    for x in slist :
        x = int(x)
        ilist.append(x)
    return ilist

@counter
@logging
@benchmark
def summate(ilist):
    s = 0
    for x in ilist :
        s = s + x
    return s

@counter
@logging
@benchmark
def average(ilist):
    s = 0
    for x in ilist :
        s = s + x
    av = s / len(ilist)
    return av

@counter
@logging
@benchmark
def faculty(n):
    if (n == 1):
        return n
    return n*faculty(n-1)
