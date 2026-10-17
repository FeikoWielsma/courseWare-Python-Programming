version = "0.1"


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self) -> None:
        print(f"Person -- firstname: {self.firstname}  lastname: {self.lastname}")


def sayhi() -> None:
    print("Hi, this is testmodules speaking.")
