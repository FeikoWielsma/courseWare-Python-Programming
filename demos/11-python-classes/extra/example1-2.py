class A:
    def __init__(self):
        print("A")
        super().__init__()


class B:
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self, arg):
        print("C", "arg=", arg)
        super().__init__()


class D(B):
    def __init__(self, arg):
        print("D", "arg=", arg)
        super().__init__()


class E(C, D):
    def __init__(self, arg):
        print("E", "arg=", arg)
        super().__init__(arg)


print("MRO:", [x.__name__ for x in E.__mro__])
E(10)
