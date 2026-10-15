class Square:
    def __init__(self, length: float) -> None:
        self.length = length

    @property
    def area(self) -> float:
        return self.length * self.length


sq = Square(5)
print(sq.area)  # no parentheses
sq.length = 6
print(sq.area)  # always current

try:
    sq.area = 50  # read-only : there is no setter
except AttributeError as e:
    print(e)
