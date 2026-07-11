# Exercise 5 : Functions

In this exercise the inline calculations are replaced by functions.

---

### Step 1

Create a project or directory named `exercise5` and a Python module `calculator5.py`. Copy the contents of the previous exercise to `calculator5.py`.

Write functions to add, subtract, multiply and divide two numbers and replace the code that does the calculations inline by a call to these functions :

```python
def add(i, j):
    z = i + j
    return z
```

Calling this function is done with :

```python
addresult = add(f1, f2)
```

### Step 2

Write a function `convertointlist` that converts a list of input characters to a list of integers :

```python
def convertointlist(slist):
    ilist = []
    for x in slist:
        x = int(x)
        ilist.append(x)
    return ilist
```

Call this function with as parameter the input list given by the user for the sum and average calculations.

Also write a function `summate` that takes a list of integers as an argument and returns the sum of the integers in that list. And write a function `average` that takes a list of integers and returns the average of these integers :

```python
def summate(ilist):
    s = 0
    for x in ilist:
        s = s + x
    return s
```

Replace the inline summation and averaging code by calls to these functions.

### Step 3

Add another calculation option to the calculator called `"Faculty"`. When the user enters this, one number should be entered and the factorial of this number should be calculated. Hereby the factorial of n is defined as n * (n-1) * (n-2) * (n-3) * ... * 1.

Create a recursive function called `faculty` to perform this calculation and call this function.
