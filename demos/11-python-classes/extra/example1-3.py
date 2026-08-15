class A:
    def __init__(self, *args, **kwargs):
        print("A")
        super().__init__(*args, **kwargs)


class B:
    def __init__(self, *args, **kwargs):
        print("B")
        # super(B, self).__init__(*args, **kwargs)


class C(A):
    def __init__(self, arg, *args, **kwargs):
        print("C", "arg=", arg)
        super().__init__(arg, *args, **kwargs)


class D(B):
    def __init__(self, arg, *args, **kwargs):
        print("D", "arg=", arg)
        super().__init__(arg, *args, **kwargs)


class E(C, D):
    def __init__(self, arg, *args, **kwargs):
        print("E", "arg=", arg)
        super().__init__(arg, *args, **kwargs)


print("MRO:", [x.__name__ for x in E.__mro__])
E(10)
