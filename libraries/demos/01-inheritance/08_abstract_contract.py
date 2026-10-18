from abc import ABC, abstractmethod


class Ability(ABC):
    @abstractmethod
    def cast(self) -> str:
        """Return the ability's action."""


class Frostbolt(Ability):
    def cast(self) -> str:
        return "Frostbolt deals frost damage"


class UnfinishedAbility(Ability):
    pass

print(Frostbolt().cast())
try:
    UnfinishedAbility()
except TypeError as error:
    print(f"TypeError: {error}")
