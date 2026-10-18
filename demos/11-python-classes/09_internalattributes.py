class Character:
    def __init__(self, name: str) -> None:
        self.name = name  # public
        self._gold = 0  # internal, by convention
        self.__auth_code = "7f3a"  # name mangled to _Character__auth_code


jaina = Character("Jaina")
print(jaina.name)
print(jaina._gold)  # works, but the underscore says: not for you
print(jaina._Character__auth_code)  # the mangled name still works

try:
    print(jaina.__auth_code)
except AttributeError as e:
    print(e)
