# Exercise 8 : Exception Handling

In this exercise the calculator is made robust against invalid input.

---

### Step 1

Create a project or directory named `exercise8` and a Python module `calculator8.py`. Copy the contents of `calculator6.py` to `calculator8.py`. Also copy the `calcu` package which now should contain comprehensions.

Write `try: except:` statements for the following cases. In all these cases the current program crashes. With exception handling we can ask for new input.

1. Division by zero.
2. Wrong input for Add, Subtract, Multiply and Divide operations.
3. Wrong input for the number for the factorial.
4. Wrong input for the list of integers.

### Step 2

Define an exception class. Then write a `try: except:` statement in which you throw and catch that specific exception. Use code from the demo directories or the internet as example code.

### Step 3

The code that we have made up to now is not very clean. We should make our script more maintainable and extensible. One big script in which everything happens is not so good. The if statements are also nested too much.

Now refactor the code so it consists of a main from where three functions are called, namely : `OneNumberCalculations`, `TwoNumberCalculations` and `MultipleNumberCalculations`. Each of these functions should get a `calcAction` string as parameter.

Write this script in the file `calculatorclean.py`. Make sure the script works exactly the same as the non-clean version.
