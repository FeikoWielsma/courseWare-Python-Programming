class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


jaina = Character("Jaina", 100)
print(jaina.health)  # read it
jaina.health = 80  # write it
print(jaina.health)
