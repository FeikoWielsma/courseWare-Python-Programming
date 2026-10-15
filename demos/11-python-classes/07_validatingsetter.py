class Square:
    def __init__(self, length: float) -> None:
        self.length = length  # goes through the setter below

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"length must not be negative, got {value}")
        self._length = value

    @property
    def area(self) -> float:
        return self.length * self.length


# The same calling code as in 06_computedproperty.py
sq = Square(5)
print(sq.area)
sq.length = 6
print(sq.area)

try:
    sq.length = -3  # accepted by the plain attribute, refused now
except ValueError as e:
    print(e)

try:
    Square(-1)  # __init__ uses the setter too
except ValueError as e:
    print(e)
