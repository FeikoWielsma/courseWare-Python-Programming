# Filename: classwithmethod.py


class Person:
    def say_hi(self) -> None:
        print("Hello, how are you?")

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def greet(self) -> None:
        print(f"Hello, world! I'm {self.name}.")


p1 = Person()
p1.say_hi()

# This short example can also be written as Person().say_hi()
Person().say_hi()

p2 = Person()
p2.set_name("pipo")
print(p2.get_name())
p2.greet()
print(p2.name)

# Person().set_name('mamaloe')
# print (Person().get_name())
# Person().greet()
# print (Person().name)
