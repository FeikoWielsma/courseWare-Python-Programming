class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    @property
    def is_alive(self) -> bool:
        return self.health > 0


hero = Character("Aria", 30)
print(hero.is_alive)  # no parentheses
hero.health = 0
print(hero.is_alive)  # always current

try:
    hero.is_alive = True  # read-only : there is no setter
except AttributeError as e:
    print(e)
