---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python Classes
---

# Object Orientation in Python

- Python is an object-oriented language :
  - Every value in Python is an object, and every object has a class
  - Classes of your own are created with the `class` keyword
- Class :
  - A blueprint for a set of related objects
  - Defines the attributes and methods that every object of the class has
  - Attributes hold data, methods are functions; both are reached with dot notation
- Object or instance :
  - An individual object of a certain class, with its own identity
  - Its state is the current value of its attributes
  - State differs per object, behavior is shared by all instances
- Inheritance :
  - A class can extend another class, inheriting its attributes and methods

---

# Example Class and Objects

- A class is a blueprint; each object has its own state :

<table>
<thead>
<tr><th></th><th>Character Class</th><th>Object Character A</th><th>Object Character B</th></tr>
</thead>
<tbody>
<tr><td rowspan="4">Instance<br/>Variables</td><td>Name</td><td>Aria</td><td>Grok</td></tr>
<tr><td>Role</td><td>Archer</td><td>Troll</td></tr>
<tr><td>Health</td><td>95</td><td>35</td></tr>
<tr><td>Position</td><td>(4, 7)</td><td>(5, 7)</td></tr>
<tr><td rowspan="3">Instance<br/>Methods</td><td colspan="3">Move Method</td></tr>
<tr><td colspan="3">Take Damage Method</td></tr>
<tr><td colspan="3">Heal Method</td></tr>
</tbody>
</table>

---

# Creating Classes

- The `class` statement creates a new class :
  - The name of the class follows the keyword `class`, then a colon
  - The indented block below it is the body of the class

```python
class Character:
    """A game character, with nothing in it yet."""

    pass  # an empty block
```

- The string on the first line of the body is the documentation string :
  - It can be read as `Character.__doc__`
- Calling the class creates an object :

```python
hero = Character()
print(hero)
```

```text
<__main__.Character object at 0x0000024A00FD8D70>
```

> `demo01 · simplestclass`

---

# Example Creating Classes and Objects

```python
class Character:
    """A character in a game, with its own health."""
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    def take_damage(self, amount: int) -> None:
        self.health = max(self.health - amount, 0)
    def heal(self, amount: int) -> None:
        self.health = min(self.health + amount, 100)
    def show_status(self) -> None:
        print(f"{self.name} : {self.health} health")
```

- To create an instance of a class :
  - Call the class by its name and pass the arguments that `__init__` accepts
- Create an object of the `Character` class :

```python
hero = Character("Aria", 100)
```

---

# Class Members

- `__init__()` :
  - The initialization method, often called the constructor
  - Called by Python when you create a new instance of this class
  - Sets the instance attributes, here `self.name` and `self.health`
- Instance methods :
  - Declared like normal functions, but the first parameter of each method is `self`
  - You do not pass `self` when you call a method, since Python adds it
- `self` is a reference to the instance :
  - Instance attributes are read and written as `self.health`
  - `hero.take_damage(10)` changes the health of `hero` and of no other character
- Python frees objects for you when nothing refers to them any more :
  - `__del__` exists and you rarely need it

---

# Creating and Using Objects

- Creating objects :

```python
hero = Character("Aria", 100)
troll = Character("Grok", 60)
```

- Access the object's methods and attributes using the dot operator :

```python
troll.take_damage(25)
hero.take_damage(10)
hero.heal(5)

hero.show_status()
troll.show_status()
```

- Result :

```text
Aria : 95 health
Grok : 35 health
```

- Each object keeps its own `health`; the methods are shared

> `demo02 · character`

---

# Accessing Attributes

- In Python you can add, remove, or modify attributes at any time :

```python
hero.shield = 10  # Add a 'shield' attribute
hero.shield = 15  # Modify 'shield' attribute
del hero.shield  # Delete 'shield' attribute
```

- Four functions do the same with an attribute name held in a string :
  - Useful when the name is only known while the program runs

```python
attr = "shield"  # an attribute name held in a variable
print(hasattr(hero, attr))  # True if the attribute exists
setattr(hero, attr, 15)  # Set or create the attribute
print(getattr(hero, attr))  # Returns the value of the attribute
delattr(hero, attr)  # Delete the attribute
print(getattr(hero, attr, "no shield"))  # The default, because the attribute is gone
```

```text
False
15
no shield
```

---

# Class Attributes and Instance Attributes

```python
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
```

- A class attribute is assigned in the class body; an instance attribute on `self`
- Reading `hero.max_health` looks on the object first, then on the class
- Assigning `hero.max_health` writes to the object; change shared data on the class
- Methods that need no instance exist as well, `@staticmethod` and `@classmethod` :
  - They are covered in the Advanced Python course

> `demo03 · classattributes`

---

# `__str__` and `__repr__`

```python
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    def __repr__(self) -> str:
        return f"Character({self.name!r}, {self.health!r})"
    def __str__(self) -> str:
        return f"{self.name} ({self.health} health)"

hero = Character("Aria", 100)
print(hero)  # str(), for people
print(repr(hero))  # repr(), for developers
print([hero])  # a list shows the repr() of its items
```

```text
Aria (100 health)
Character('Aria', 100)
[Character('Aria', 100)]
```

- `__str__` is used by `print()`, `str()` and f-strings
- `__repr__` is used by the interactive prompt, by containers and by `!r` :
  - Make it look like the call that creates the object; `str()` falls back to it

> `demo04 · strrepr`

---

# Attributes Are Public

- An attribute set in `__init__` is public, and that is fine :
  - Any code that has the object can read it and assign to it
  - No methods are written to get or set it

```python
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

hero = Character("Aria", 100)
print(hero.health)  # read it
hero.health = 80  # write it
print(hero.health)
```

```text
100
80
```

> `demo05 · publicattributes`

---

# A Computed Attribute

- Whether a character is alive depends on its health :
  - As a method, `def is_alive(self)`, it is called as `hero.is_alive()`
  - With `@property` above the `def`, it is read as `hero.is_alive`, like an attribute

```python
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    @property
    def is_alive(self) -> bool:
        return self.health > 0

hero = Character("Aria", 30)
print(hero.is_alive)  # no parentheses
hero.health = 0
print(hero.is_alive)  # always current
hero.is_alive = True  # read-only : there is no setter
```

```text
True
False
AttributeError: property 'is_alive' of 'Character' object has no setter
```

> `demo06 · computedproperty`

---

# When a Plain Attribute Is Not Enough

- The `Character` so far accepts any health, `hero.health = -20` included
- The fix makes `health` a property whose setter checks the value :

```python
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health  # goes through the setter below
    @property
    def health(self) -> int:
        return self._health
    @health.setter
    def health(self, value: int) -> None:
        if not 0 <= value <= 100:
            raise ValueError(f"health must be between 0 and 100, got {value}")
        self._health = value
```

- The value is stored in `self._health`, the property's own storage
- The code that uses the class does not change :
  - `hero.health = 0` still works, and `hero.health = -20` now raises `ValueError`

> `demo07 · validatingsetter`

---

# The Rule of Thumb

- Start with a plain attribute :
  - Do not write getter and setter methods in advance
- Turn it into a property the day it needs a rule :
  - A check on the value, or a value computed from other attributes
  - The calling code keeps writing `hero.health`, so nothing else changes
- The property keeps its value in an attribute with a leading underscore :
  - `_health` is internal to the class, by convention

```mermaid
flowchart LR
  A[calling code] -->|hero.health = 80| B[health property<br/>checks the value] --> C[self._health]
```

---

# Internal Attributes

- Python has no keyword that makes an attribute private :
  - A leading underscore, `_gold`, means internal, by convention
  - Code outside the class can reach it, and is expected not to
- Two leading underscores, `__save_key`, make Python rename the attribute to `_Character__save_key`

```python
class Character:
    def __init__(self, name: str) -> None:
        self.name = name  # public
        self._gold = 0  # internal, by convention
        self.__save_key = "7f3a"  # name mangled to _Character__save_key

hero = Character("Aria")
print(hero.name)
print(hero._gold)  # works, but the underscore says: not for you
print(hero._Character__save_key)  # the mangled name still works
```

```text
Aria
0
7f3a
```

> `demo08 · internalattributes`

---

# A Class Can Extend Another

```python
class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
    def describe(self) -> str:
        return f"{self.name} has {self.health} health"

class Wizard(Character):
    def __init__(self, name: str, health: int, spells: list[str]) -> None:
        super().__init__(name, health)  # the Character part
        self.spells = spells  # what a Wizard adds
    def describe(self) -> str:  # replaces Character.describe
        return f"{super().describe()} and knows {len(self.spells)} spells"
```

- `Wizard` inherits every method of `Character`, adds to it and may replace methods
- `super().__init__(...)` runs the `Character` initialization, so `name` and `health` are set
- `Wizard("Lumi", 70, ["fireball", "heal"]).describe()` returns :
  - `Lumi has 70 health and knows 2 spells`
- Inheritance in depth is covered in the Advanced Python course

> `demo09 · inheritance`

---

# Summary : Python Classes

- Classes are blueprints for a set of related objects :
  - Define both attributes and methods and are created with the `class` keyword
- Objects are instances of classes :
  - Each object has its own state and identity, instance methods have a `self` parameter
- The initialization method is named `__init__()` :
  - Called by Python when the class is called to create an object
- Instance attributes belong to one object, class attributes are shared by all instances
- `__str__` and `__repr__` decide how an object is printed
- Attributes are public; a property adds a rule without changing the calling code :
  - Start with a plain attribute, turn it into a property the day it needs a rule
- A leading underscore marks an attribute as internal, by convention
- A class can extend another, and calls `super().__init__()` to set up the parent part

> `exercise11 · Python Classes`
