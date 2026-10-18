class Character:
    def __init__(self, name: str) -> None:
        self.name = name  # public
        self._gold = 0  # internal, by convention
        self.__save_key = "7f3a"  # name mangled to _Character__save_key


hero = Character("Aria")
print(hero.name)
print(hero._gold)  # works, but the underscore says: not for you
print(hero._Character__save_key)  # the mangled name still works

try:
    print(hero.__save_key)
except AttributeError as e:
    print(e)
