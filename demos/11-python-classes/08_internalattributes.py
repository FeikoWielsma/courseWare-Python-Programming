class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner  # public
        self._balance = 0  # internal, by convention
        self.__pin = "1234"  # name mangled to _Account__pin


acc = Account("Albert")
print(acc.owner)
print(acc._balance)  # works, but the underscore says: not for you
print(acc._Account__pin)  # the mangled name still works

try:
    print(acc.__pin)
except AttributeError as e:
    print(e)
