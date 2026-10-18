class Character:
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> None:
        print(f"I am {self.name}")


jaina = Character("Jaina")
thrall = Character("Thrall")
jaina.introduce()
thrall.introduce()
print(jaina.name)
