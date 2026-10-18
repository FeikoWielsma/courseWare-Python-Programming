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


class Warrior(Character):
    def attack(self) -> str:
        return f"{self.name} uses Heroic Strike"


class Priest(Character):
    def attack(self) -> str:
        return f"{self.name} casts Smite"

raid: list[Character] = [Mage("Jaina"), Warrior("Varian"), Priest("Anduin")]
for member in raid:
    print(member.attack())
