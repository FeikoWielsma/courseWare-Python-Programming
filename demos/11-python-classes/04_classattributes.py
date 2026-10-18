class Character:
    max_level = 60  # class attribute, one value shared by every character

    def __init__(self, name: str) -> None:
        self.name = name  # instance attribute, one value per character


jaina = Character("Jaina")
thrall = Character("Thrall")
print(jaina.name, thrall.name)  # Jaina Thrall
print(jaina.max_level, thrall.max_level)  # 60 60

Character.max_level = 70  # an expansion raises the cap for everyone
print(jaina.max_level, thrall.max_level)  # 70 70

jaina.max_level = 80  # creates an instance attribute on jaina only
print(jaina.max_level, thrall.max_level, Character.max_level)  # 80 70 70
