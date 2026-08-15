class A:
    def __init__(self):
        print(
            "A",
        )
        super().__init__()



class B:
    def __init__(self):
        print(
            "B",
        )
        super().__init__()



# some other module defines this class, not knowing about super()


class C(A, B):
    def __init__(self):
        print(
            "C",
        )
        A.__init__(self)
        B.__init__(self)

    #        super(D, self).__init__()


print("MRO:", [x.__name__ for x in C.__mro__])
print(
    "Calls:",
)
C()
print()
