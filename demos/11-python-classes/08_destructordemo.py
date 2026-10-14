class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __del__(self) -> None:
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the objects
print(pt1, pt2, pt3)  # the default repr shows the same id, in hex
del pt1
del pt2
print("pt1 and pt2 are gone, but pt3 still refers to the object")
del pt3  # the last reference: __del__ runs now
print("End of program")
