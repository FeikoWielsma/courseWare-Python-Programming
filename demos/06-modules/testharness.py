version = "0.1"


class Person:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show(self) -> None:
        print(f"Person -- firstname: {self.firstname}  lastname: {self.lastname}")


def sayhi() -> None:
    print("Hi, this is testmodules speaking.")


def main() -> None:
    print(version)
    print("=" * 30)
    sayhi()
    print("=" * 30)
    person = Person("Robert", "Oppenheimer")
    person.show()


if __name__ == "__main__":
    main()
