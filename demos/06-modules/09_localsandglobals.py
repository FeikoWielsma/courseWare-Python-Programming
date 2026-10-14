x = 1


def f():
    y = 1
    print("Globals from f")
    print(globals().keys())
    print("Locals from f")
    print(locals().keys())


f()
