class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __repr__(self) -> str:
        return f"Character({self.name!r}, {self.health!r})"

    def __str__(self) -> str:
        return f"{self.name} ({self.health} health)"


jaina = Character("Jaina", 100)
print(jaina)  # str(), for people
print(f"Player one is {jaina}")  # str() again
print(repr(jaina))  # repr(), for developers
print([jaina])  # a list shows the repr() of its items
