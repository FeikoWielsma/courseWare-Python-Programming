class Character:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100

    def attack(self) -> str:
        return f"{self.name} attacks"


class Mage(Character):
    def __init__(self, name: str, mana: int = 100) -> None:
        super().__init__(name)
        self.mana: int = mana

    def attack(self) -> str:
        return f"{self.name} casts Frostbolt"

jaina = Mage("Jaina")
print(jaina.attack())
print(Character.attack(jaina))
print([cls.__name__ for cls in Mage.__mro__])
print(Mage.__str__ is object.__str__)
