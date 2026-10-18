
class Mount:
    def __init__(self, name: str) -> None:
        self.name: str = name


class Inventory:
    def __init__(self) -> None:
        self.items: list[str] = []


class Character:
    def __init__(self, name: str, mount: Mount) -> None:
        self.name: str = name
        self.mount: Mount = mount
        self.inventory: Inventory = Inventory()


jaina = Character("Jaina", Mount("Gryphon"))
jaina.inventory.items.append("Healing Potion")
print(jaina.mount.name)
print(jaina.inventory.items)
