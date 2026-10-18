class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __repr__(self) -> str:
        return f"Character({self.name!r}, {self.health!r})"

    def __str__(self) -> str:
        return f"{self.name} ({self.health} health)"


hero = Character("Aria", 100)
print(hero)  # str(), for people
print(f"Player one is {hero}")  # str() again
print(repr(hero))  # repr(), for developers
print([hero])  # a list shows the repr() of its items
