# Exercise 1 : Inheritance and Class Design

A fundamentals course ends with an `Employee` class much like the one below. In this exercise you keep that class and grow a family of employees around it, so that a payroll run works the same whether a person is paid by the hour, by the month, or by the hour plus a bonus. Inheritance is the only new idea here; everything else is ordinary class work.

Work in a folder of your own, for example `work/01-inheritance/`. The reference solution is in `solutions/solution01-inheritance/`.

---

### Step 1 : The employee you already have

Create `employee.py` and put a plain `Employee` class in it, with a name, an ID and a `calc_salary` method that returns zero. Nothing here is new :

```python
class Employee:
    def __init__(self, name: str, employee_id: int) -> None:
        self.name: str = name
        self.employee_id: int = employee_id

    def calc_salary(self) -> float:
        return 0.0
```

Add a `main` function that builds one employee and prints the name, the ID and the salary, and call it from the usual guard :

```python
if __name__ == "__main__":
    main()
```

Run it with `uv run employee.py`. One line of output is the whole goal of this step; it proves the file is where you think it is and that `uv` is working.

### Step 2 : An employee paid by the hour

Add a second class in the same file. `WageEmployee` is a kind of `Employee`, so it names `Employee` as its base class, adds an hourly wage and a number of hours, and replaces `calc_salary` with a version that multiplies the two :

```python
class WageEmployee(Employee):
    def __init__(self, name: str, employee_id: int, wage: float, hours: float) -> None:
        super().__init__(name, employee_id)
        self.wage: float = wage
        self.hours: float = hours
```

Write `calc_salary` yourself. Then create a `WageEmployee`, print its `name`, and notice that you never wrote a `name` attribute in this class.

Now delete the `super().__init__(...)` line, run the program again, and read the error carefully. Put the line back. That error is the single most common mistake with inheritance, and it is worth recognising once on purpose.

### Step 3 : Two more kinds of employee

Add `ManagerEmployee`, which is also a kind of `Employee` but is paid a fixed amount each month. Its `calc_salary` returns that amount.

Then add `ProgrammerEmployee`. A programmer is paid like a wage employee and gets a bonus on top, so its base class is `WageEmployee` rather than `Employee`. Its `calc_salary` should reuse the version it inherits rather than repeating the multiplication :

```python
class ProgrammerEmployee(WageEmployee):
    def calc_salary(self) -> float:
        base = super().calc_salary()
        return base + ...
```

Give it `lines` and `bugs` attributes and decide for yourself what the bonus is worth. Something like one euro a line, minus twenty a bug, is fine.

Print the salary of one of each class.

### Step 4 : Printing an employee properly

Put `__str__` and `__repr__` on `Employee` only, and check that all four classes get them :

```python
    def __str__(self) -> str:
        return f"{self.name} (#{self.employee_id})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, id={self.employee_id})"
```

Use `type(self).__name__` rather than writing the class name as text, so that a `ManagerEmployee` says so. Print one employee directly, then print a list of employees, and note which of the two methods each case used.

### Step 5 : One loop over all of them

Create `company.py` next to `employee.py`, import the classes from it, and build a list holding one of each :

```python
from employee import Employee, ManagerEmployee, ProgrammerEmployee, WageEmployee
```

Write a `payroll` function that takes a `list[Employee]`, loops over it, prints each employee with the salary, and returns the total :

```python
def payroll(staff: list[Employee]) -> float:
    ...
```

The body must not mention `WageEmployee`, `ManagerEmployee` or `ProgrammerEmployee` anywhere. Each call to `calc_salary` finds the right version on its own, and that is polymorphism.

### Step 6 : Asking what an employee is

Add a function that counts how many of the staff are managers, using `isinstance` rather than comparing `type(...)` with a class. Print the count.

Then check `isinstance(a_programmer, WageEmployee)` and explain to yourself why it is true. Check `issubclass(ProgrammerEmployee, Employee)` as well.

### Step 7 : Turning the base class into a contract

Right now nothing stops someone writing a new kind of employee and forgetting `calc_salary`; the payroll would silently pay them zero. Make that impossible by turning `Employee` into an abstract base class :

```python
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calc_salary(self) -> float:
        """Every kind of employee has to say how it is paid."""
```

Keep `__init__`, `__str__` and `__repr__` concrete; only `calc_salary` becomes abstract. Then try to create a plain `Employee(...)` and read the `TypeError`. Write a `SalesEmployee` that inherits from `Employee` but supplies no `calc_salary`, try to construct one, and confirm the failure happens at construction rather than at payroll time.

Remove `SalesEmployee` again, or finish it, whichever you prefer.

### Step 8 : Optional, a company that has employees

A `Company` is not a kind of employee, so it must not inherit from one. It holds a list of them instead, which is composition :

```python
class Company:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.staff: list[Employee] = []

    def hire(self, employee: Employee) -> None:
        ...
```

Give it `hire`, `fire` and a `payroll` method that reuses the function from Step 5. Then add a `breakdown` method that reports the total per class, using `type(employee).__name__` as the key of a dictionary.

Say both relationships out loud as a check on the design : a programmer *is a* wage employee, and a company *has* employees.
