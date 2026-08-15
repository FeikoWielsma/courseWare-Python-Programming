class A:
    count = 0

    def __init__(self, name: str) -> None:
        self.name = name

    def set_name(self, name: str) -> None:
        print(f"setting name: {name}")
        self.name = name

    def get_name(self) -> str:
        print(f"getting name: {self.name}")
        return self.name

    objname = property(get_name, set_name)


def test():
    a = A("apple")
    print(f"name: {a.objname}")
    a.objname = "banana"
    print(f"name: {a.objname}")


test()
