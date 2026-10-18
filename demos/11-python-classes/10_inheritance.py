class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def describe(self) -> str:
        return f"{self.name} has {self.health} health"


class Mage(Character):
    def __init__(self, name: str, health: int, spells: list[str]) -> None:
        super().__init__(name, health)  # the Character part
        self.spells = spells  # what a Mage adds

    def describe(self) -> str:  # replaces Character.describe
        return f"{super().describe()} and knows {len(self.spells)} spells"


thrall = Character("Thrall", 100)
jaina = Mage("Jaina", 70, ["Fireball", "Frostbolt", "Blizzard"])
print(thrall.describe())
print(jaina.describe())
print(jaina.name)  # set by Character.__init__
print(isinstance(jaina, Character))
