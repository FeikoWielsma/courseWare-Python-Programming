class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


hero = Character("Aria", 100)
print(hero.health)  # read it
hero.health = 80  # write it
print(hero.health)
