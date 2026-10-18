class Character:
    """A character in a game, with its own health."""

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)

    def heal(self, amount: int) -> None:
        self.health = min(self.health + amount, 100)

    def show_status(self) -> None:
        print(f"{self.name} : {self.health} health")


hero = Character("Aria", 100)
troll = Character("Grok", 60)

troll.take_damage(25)
hero.take_damage(10)
hero.heal(5)

hero.show_status()
troll.show_status()

hero.shield = 10  # Add a 'shield' attribute
hero.shield = 15  # Modify 'shield' attribute
del hero.shield  # Delete 'shield' attribute

attr = "shield"  # an attribute name held in a variable
print(hasattr(hero, attr))  # True if the attribute exists
setattr(hero, attr, 15)  # Set or create the attribute
print(getattr(hero, attr))  # Returns the value of the attribute
delattr(hero, attr)  # Delete the attribute
print(getattr(hero, attr, "no shield"))  # The default, because the attribute is gone
