# Filename: classwithinit.py


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)


p = Person("Pipo")
p.say_hi()

# This short example can also be written as Person('Pipo').say_hi()
