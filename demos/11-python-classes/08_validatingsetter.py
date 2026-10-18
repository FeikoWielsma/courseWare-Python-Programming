class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health  # goes through the setter below

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        if not 0 <= value <= 100:
            raise ValueError(f"health must be between 0 and 100, got {value}")
        self._health = value

    @property
    def is_alive(self) -> bool:
        return self.health > 0


# The same calling code as in 06_computedproperty.py
jaina = Character("Jaina", 30)
print(jaina.is_alive)
jaina.health = 0
print(jaina.is_alive)

try:
    jaina.health = -20  # accepted by the plain attribute, refused now
except ValueError as e:
    print(e)

try:
    Character("Hogger", 500)  # __init__ uses the setter too
except ValueError as e:
    print(e)
