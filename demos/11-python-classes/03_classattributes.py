class Character:
    max_health = 100  # class attribute, one value shared by every character

    def __init__(self, name: str) -> None:
        self.name = name  # instance attribute, one value per character


hero = Character("Aria")
mage = Character("Lumi")
print(hero.name, mage.name)  # Aria Lumi
print(hero.max_health, mage.max_health)  # 100 100

Character.max_health = 120  # changes the shared value
print(hero.max_health, mage.max_health)  # 120 120

hero.max_health = 150  # creates an instance attribute on hero only
print(hero.max_health, mage.max_health, Character.max_health)  # 150 120 120
