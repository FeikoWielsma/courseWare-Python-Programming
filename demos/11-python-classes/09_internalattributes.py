class Character:
    def __init__(self, name: str) -> None:
        self.name = name  # public
        self._gold = 0  # internal, by convention


jaina = Character("Jaina")
print(jaina.name)
print(jaina._gold)  # works, but the underscore says: not for you
