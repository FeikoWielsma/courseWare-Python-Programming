# from math import *

x = 1


def f():
    y = 1
    print("Globals from f")
    # print(globals())
    print(globals().keys())
    print("Locals from f")
    # print(locals())
    print(locals().keys())


f()
