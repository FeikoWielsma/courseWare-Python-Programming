# Exercise 4 : Control Flow

In this exercise the calculator becomes interactive : the user chooses the type of calculation.

---

### Step 1

Create a project or directory named `exercise4` and a Python module `calculator4.py`. Copy the contents of step 3 of the previous exercise to `calculator4.py`.

Now ask the user, beside the numbers for the calculations, also which type of calculation the user wants to perform. Use `if`, `else` and `elif` statements to determine which branch of the code must be entered. If the user enters `"Quit"` the application should stop :

```python
resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
while True:
    calcAction = input("What type of calculation do you want to do : ")
    if calcAction == "Quit":
        break
    else:
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calcAction == "Add":
            addresult = f1 + f2
            addlist = [f1, f2, addresult]
            resdict["Add"] = resdict["Add"] + addlist
        elif calcAction == "Subtract":
            ...
```

### Step 2

Now add an option to calculate the sum and average of a list of numbers. Copy part of the code from step 4 of exercise 3 to convert a list of strings to a list of integers. Based on the input of the desired calculation type, you will have to make a distinction between the input of a list of numbers or only two numbers :

```python
elif (calcAction == "Sum") or (calcAction == "Average"):
    s = input("Give a set of numbers separated by space characters : ")
```

Now calculate the sum or the average of the list of numbers in a `for` loop. Do not use `sum` as a variable name since this is a reserved word; use `summation` instead. For the calculation of the sum the code could look as follows :

```python
summation = 0
average = 0
if calcAction == "Sum":
    for x in slist:
        x = int(x)
        summation = summation + x
        intlist.append(x)
    print (f"Sum of list {intlist} is {summation}")
```

### Step 3

Replace the `while True` statement at the beginning of the code by a test on the input of the calculation type. Stop the while loop when the input is `"Quit"` :

```python
calcAction = "Continue"
while calcAction != "Quit":
    calcAction = input("What type of calculation do you want to do : ")
```

Also add an `else` statement to the while loop that gets executed when the while loop stops :

```python
else:
    print ("Thank you for using our software")
```
