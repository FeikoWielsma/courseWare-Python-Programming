
class Mage:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.mana: int = 100


class Warrior:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.rage: int = 0


print(vars(Mage("Jaina")))
print(vars(Warrior("Varian")))
