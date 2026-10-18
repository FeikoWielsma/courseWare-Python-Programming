class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    @property
    def is_alive(self) -> bool:
        return self.health > 0


jaina = Character("Jaina", 30)
print(jaina.is_alive)  # no parentheses
jaina.health = 0
print(jaina.is_alive)  # always current

try:
    jaina.is_alive = True  # read-only : there is no setter
except AttributeError as e:
    print(e)
