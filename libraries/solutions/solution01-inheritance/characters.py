from abc import ABC, abstractmethod


class Mount:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Inventory:
    def __init__(self) -> None:
        self.items: list[str] = []


class Character(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.inventory: Inventory = Inventory()
        self.mount: Mount | None = None

    @abstractmethod
    def attack(self) -> str:
        """Describe this character's action."""

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"


class Mage(Character):
    def __init__(self, name: str, mana: int = 100) -> None:
        super().__init__(name)
        self.mana: int = mana

    def attack(self) -> str:
        return f"{self.name} casts Frostbolt"


class Warrior(Character):
    def __init__(self, name: str, rage: int = 0) -> None:
        super().__init__(name)
        self.rage: int = rage

    def attack(self) -> str:
        return f"{self.name} uses Heroic Strike"


class Priest(Character):
    def attack(self) -> str:
        return f"{self.name} casts Smite"


if __name__ == "__main__":
    for member in (Mage("Jaina"), Warrior("Varian"), Priest("Anduin")):
        print(member.attack())
