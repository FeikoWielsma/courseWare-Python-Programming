class Character:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"


class Mage(Character):
    pass

jaina = Mage("Jaina")
print(jaina)
print(repr(jaina))
print([jaina])
