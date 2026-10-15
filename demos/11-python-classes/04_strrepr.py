class Car:
    def __init__(self, plate: str, color: str) -> None:
        self.plate = plate
        self.color = color

    def __repr__(self) -> str:
        return f"Car({self.plate!r}, {self.color!r})"

    def __str__(self) -> str:
        return f"{self.color} car {self.plate}"


car = Car("ABC 111", "Blue")
print(car)  # str(), for people
print(f"I drive a {car}")  # str() again
print(repr(car))  # repr(), for developers
print([car])  # a list shows the repr() of its items
