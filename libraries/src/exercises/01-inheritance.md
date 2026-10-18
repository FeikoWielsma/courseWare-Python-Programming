# Exercise 1 : A Guild Roster

Build a roster whose members share character state but supply different attacks.
Health, mana and rage are simplified teaching values, not a model of the game.
Start from `exercises/starters/01-inheritance/` and run from `libraries/`.
The final solution is in `solutions/solution01-inheritance/`.

### Step 1 : Define a character

Create `characters.py` with a plain `Character` class. Store `name` and an
initial `health` of 100. Add `attack() -> str` returning a description.
Construct a character and print its attributes and attack.

:::hint
The slides *Base Classes and Subclasses* and *Inherited Members* show the
shared attributes and method on `Character`.
:::

### Step 2 : Add specialisations

Create `Mage(Character)` with `mana`, and `Warrior(Character)` with `rage`.
Call `super().__init__(name)` in each initialiser. Override `attack` so a mage
casts Frostbolt and a warrior uses Heroic Strike. Add `Priest(Character)` with
a Smite attack; it can inherit the base initialiser unchanged.

:::hint
The slides *Constructor Chaining* and *Overriding Methods* show `super` and
method replacement. Demo `polymorphism` includes all three subclasses.
:::

### Step 3 : Give objects a display

Implement `__str__` and `__repr__` on `Character`. Print one mage directly,
then a list containing it. Check which method each display uses.
Also compare `isinstance(mage, Character)` with `type(mage) is Character`.

:::hint
The slides *str and repr* and *isinstance and issubclass* show these operations.
:::

### Step 4 : Build the roster

Create `guild.py`. A `Guild` holds a `list[Character]`. Give it `recruit` to add
a member and `report` to return the members' attack descriptions. The report
must call `member.attack()` without checking a member's subclass.
Recruit Jaina as a mage, Varian as a warrior and Anduin as a priest, then print
the report.

:::hint
The slide *Polymorphism* shows one loop calling each object's implementation.
*Composition* shows one object holding other objects.
:::

### Step 5 : Enforce the interface

Make `Character` an abstract base class with abstract `attack`. Keep its
initialiser and display methods concrete. Try constructing `Character` and an
unfinished subclass, then remove those failing calls. Confirm that all three
complete subclasses still work with the roster.

:::hint
The slides *Abstract Base Classes* and *Enforcing the Contract* show `ABC`,
`abstractmethod` and the construction error for an incomplete subclass.
:::

### Step 6 : Add belongings

Add `Mount` and `Inventory`. A character has an inventory and may have a mount;
it does not inherit from either class. Give Jaina a Gryphon and a Healing Potion.
Print the mount name and inventory contents through the character attributes.

:::hint
The slide *Composition* and demo `composition` show collaborator attributes.
:::

### If time permits

Count mages with `isinstance`. Add another concrete character class without
changing `Guild.report`. Give the inventory a method to add an item instead of
appending to its list from the caller.

:::hint
The slides *isinstance and issubclass* and *Polymorphism* show how these changes
keep the roster independent of specific subclasses.
:::
