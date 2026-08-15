class C:
    count = 0  # number of times C.__init__ called

    def __init__(self) -> None:
        C.count = C.count + 1

    def getcount(self) -> int:
        return C.count  # or return self.count


c1 = C()
print("Current count:", c1.getcount())
c2 = C()
# print  'Current count:', C.getcount()
print("Current count:", c1.getcount())
