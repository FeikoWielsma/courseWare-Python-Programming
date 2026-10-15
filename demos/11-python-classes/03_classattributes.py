class Car:
    wheels = 4  # class attribute, one value shared by every car

    def __init__(self, plate: str) -> None:
        self.plate = plate  # instance attribute, one value per car


a = Car("ABC 111")
b = Car("XYX 123")
print(a.plate, b.plate)  # ABC 111 XYX 123
print(a.wheels, b.wheels)  # 4 4

Car.wheels = 6  # changes the shared value
print(a.wheels, b.wheels)  # 6 6

a.wheels = 3  # creates an instance attribute on a only
print(a.wheels, b.wheels, Car.wheels)  # 3 6 6
