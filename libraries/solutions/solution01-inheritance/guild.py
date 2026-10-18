from characters import Character, Mage, Mount, Priest, Warrior


class Guild:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.members: list[Character] = []

    def recruit(self, member: Character) -> None:
        self.members.append(member)

    def report(self) -> list[str]:
        return [member.attack() for member in self.members]


def main() -> None:
    guild = Guild("Practice raid")
    jaina = Mage("Jaina", mana=80)
    jaina.mount = Mount("Gryphon")
    jaina.inventory.items.append("Healing Potion")
    for member in (jaina, Warrior("Varian"), Priest("Anduin")):
        guild.recruit(member)
    for action in guild.report():
        print(action)
    print(jaina.mount.name, jaina.inventory.items)
    print(isinstance(jaina, Character), issubclass(Mage, Character))


if __name__ == "__main__":
    main()
