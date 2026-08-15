<!-- appendix -->

# Exercise 12 : Type Hinting

In this exercise you annotate code you have already written, and let a checker read the annotations for you. Work in the `course-work` project you created in Exercise 1.

---

### Step 1 : Install the checker

`mypy` is a development dependency, so add it to the project with the `--dev` flag :

```bash
uv add --dev mypy
```

### Step 2 : Annotate a function

Create a module `shapes12.py` with two functions and no annotations at all :

```python
def area(width, height):
    return width * height


def describe(name, area):
    return f"{name} has an area of {area}"


print(describe("kitchen", area(3.0, 4.0)))
```

Run it with `uv run python shapes12.py` and confirm it works. Now annotate both functions. Every parameter takes a colon and a type, and the result takes an arrow :

```python
def area(width: float, height: float) -> float:
    ...
```

Do the same for `describe`, which takes a string and a number and returns a string. Run the program again and confirm the output has not changed. Annotations do not alter what the program does.

---

### Step 3 : Let the checker find a mistake

Run the checker over the module :

```bash
uv run mypy shapes12.py
```

It should report nothing. Now introduce a mistake on purpose. Change the last line so that it passes the name and the area the wrong way round :

```python
print(describe(area(3.0, 4.0), "kitchen"))
```

Run the program. Notice that Python is perfectly happy and prints nonsense. Now run `uv run mypy shapes12.py` again. The checker reports the mismatch and names the argument that is wrong, without the program having run at all. Put the call back the way it was.

### Step 4 : Annotate a collection

Add a function that takes a list of numbers and returns their average :

```python
def average(values):
    return sum(values) / len(values)
```

Annotate it. The parameter is a list of floating point numbers, written `list[float]`, and the result is a `float`. Call it with `average([1.0, 2.0, 3.0])` and check it with `mypy`.

Then call it with a list of strings, `average(["a", "b"])`, and run `mypy` again. The checker reports the mismatch even though the offending value is inside a list.

---

### Step 5 : A value that may be absent

Add a function that greets someone whose name you may not know :

```python
def greet(name=None):
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"
```

Annotating this as `name: str = None` would be a lie, because `None` is not a `str`. Write it as `name: str | None = None` instead, and give the function a `-> str` result. Confirm with `mypy` that both `greet()` and `greet("Alice")` are accepted.

### Step 6 : Annotate a class

Take the `Employee` class from Exercise 11 and annotate its `__init__` method. The `self` parameter is never annotated. A method that returns nothing is annotated `-> None` :

```python
class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
```

Annotate the other methods as well, then run `mypy` over the module and fix whatever it reports.

**If time permits** : run `uv run mypy` over one of your solutions from an earlier exercise, with no annotations added at all. Notice how little it can say. Then annotate one function and watch how much further it can reason from that single signature.
