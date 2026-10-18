class Character:
    """A World of Warcraft character, with its own health."""

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)

    def heal(self, amount: int) -> None:
        self.health = min(self.health + amount, 100)

    def show_status(self) -> None:
        print(f"{self.name} : {self.health} health")


jaina = Character("Jaina", 100)
hogger = Character("Hogger", 60)

hogger.take_damage(25)
jaina.take_damage(10)
jaina.heal(5)

jaina.show_status()
hogger.show_status()

jaina.mount = "Gryphon"  # Add a 'mount' attribute
jaina.mount = "Swift Gryphon"  # Modify 'mount' attribute
del jaina.mount  # Delete 'mount' attribute

attr = "mount"  # an attribute name held in a variable
print(hasattr(jaina, attr))  # True if the attribute exists
setattr(jaina, attr, "Swift Gryphon")  # Set or create the attribute
print(getattr(jaina, attr))  # Returns the value of the attribute
delattr(jaina, attr)  # Delete the attribute
print(getattr(jaina, attr, "no mount"))  # The default, because the attribute is gone
