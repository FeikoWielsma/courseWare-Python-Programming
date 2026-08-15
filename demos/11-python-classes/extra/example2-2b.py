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
class F1(A, B, N):
    def __init__(self):
        print("F1", end=" ")
        super().__init__()

class F2(A, N, B):
    def __init__(self):
        print("F2", end=" ")
        super().__init__()

class F3(N, A, B):
    def __init__(self):
        print("F3", end=" ")
        super().__init__()

class F4(A, B, N, M):
    def __init__(self):
        print("F3", end=" ")
        super().__init__()

        
def test(cl):
    print("MRO:", [x.__name__ for x in cl.__mro__])
    print("Calls:", end=" ")
    cl()
    print()
test(F1)
test(F2)
test(F3)
test(F4)
