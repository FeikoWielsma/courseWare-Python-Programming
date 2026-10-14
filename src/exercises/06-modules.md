# Exercise 6 : Modules

In this exercise the calculation functions are moved to their own module and package.

---

### Step 1

Create a project or directory named `exercise6` and a Python module `calculator6.py`. Copy the contents of `calculator5.py` from the previous exercise to `calculator6.py`.

Next create a Python module `calculations.py`. Remove the function definitions from `calculator6.py` and put them into `calculations.py`. As a result all function calls in `calculator6.py` will give errors because they are calling undefined functions.

Resolve the errors by importing the calculations module with an import statement in the first line of `calculator6.py` :

```python
import calculations
```

This is not enough. You will also need to prefix all function names with the module name where they come from :

```python
addresult = calculations.add(f1, f2)
```

### Step 2

It is inconvenient to put the module name as prefix before the function name. Therefore there is an alternative syntax called `from <module> import <name>`. Now change to this alternative and name all the function names that must be imported :

```python
from calculations import (
    faculty,
    convert_to_int_list,
    summate,
    average,
    add,
    subtract,
    multiply,
    divide,
)
```

As a result the prefixes before the method calls can be removed in `calculator6.py`.

### Step 3

Finally make a `calcu` package. Put the `calculations.py` module in this package, edit the `__init__.py` file and import the functions from the package in `calculator6.py`.
