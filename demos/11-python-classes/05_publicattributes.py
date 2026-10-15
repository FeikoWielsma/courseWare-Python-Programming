class Square:
    def __init__(self, length: float) -> None:
        self.length = length


sq = Square(5)
print(sq.length)  # read it
sq.length = 6  # write it
print(sq.length)
