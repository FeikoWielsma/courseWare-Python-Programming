class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def describe(self) -> str:
        return f"{self.name} has {self.health} health"


class Wizard(Character):
    def __init__(self, name: str, health: int, spells: list[str]) -> None:
        super().__init__(name, health)  # the Character part
        self.spells = spells  # what a Wizard adds

    def describe(self) -> str:  # replaces Character.describe
        return f"{super().describe()} and knows {len(self.spells)} spells"


knight = Character("Brom", 100)
mage = Wizard("Lumi", 70, ["fireball", "heal"])
print(knight.describe())
print(mage.describe())
print(mage.name)  # set by Character.__init__
print(isinstance(mage, Character))
