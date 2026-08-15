class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()

class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()

class N:
    def __init__(self):
        print("N", end=" ")
class M:
    def __init__(self):
        print("M", end=" ")
class F1(A, N):
    def __init__(self):
        print("G1", end=" ")
        super().__init__()
class F2(B, M):
    def __init__(self):
        print("G2", end=" ")
        super().__init__()

class G(F1, F2):
    def __init__(self):
        print("G", end=" ")
        super().__init__()


def test(cl):
    print("MRO:", [x.__name__ for x in cl.__mro__])
    print("Calls:", end=" ")
    cl()
    print()
test(G)
