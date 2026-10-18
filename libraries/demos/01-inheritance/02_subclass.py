class Character:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100

    def attack(self) -> str:
        return f"{self.name} attacks"

class Mage(Character):
    pass

jaina = Mage("Jaina")
print(jaina.name, jaina.health)
print(jaina.attack())
