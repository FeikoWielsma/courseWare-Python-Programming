# Exercise 2 : Variables and Data Types

In this exercise you build the first version of the calculator application that you will extend throughout the course.

---

### Step 1

Create a directory or project named `exercise2`. Next create a Python module `calculator2.py` in this directory and create two variables `nr1` and `nr2`. Assign integer values to them as follows :

```python
nr1 = 16
nr2 = 23
```

Use your own values if you like. Print the values, the type and the memory location of the variables with :

```python
print(nr1)
print(nr2)
print(type(nr1))
print(type(nr2))
print(id(nr1))
print(id(nr2))
```

You should see that the type of the variables is `<class 'int'>`. The `id` function gives some numeric value which actually indicates the memory address in a default Python implementation.

Now change the values of the variables by assigning them to a new value and print the memory location of the variables again with the `id` function. Notice that the id of the variables has changed just by assigning them. This illustrates the fact that integer variables are read-only : they cannot change once they are created. When you change an integer variable you actually create a new one.

### Step 2

Next perform arithmetic operations on the variables by adding, subtracting, multiplying and dividing them. Store the result of these operations in other variables. An example for the addition operation is :

```python
addresult = nr1 + nr2
```

Display the results of the operations with an explanatory message :

```python
print("The result of the addition of : " + str(nr1) + " and " + str(nr2) + " is : ")
print(addresult)
```

Notice the conversion function `str` that turns an integer into a string, so that it can be added to other strings.

As an alternative you can also use the string format operator `%` for printing values in a string :

```python
print("The result of the addition of : %d and %d is : " % (nr1, nr2))
```

A third alternative is to use the new style of formatting in Python 3 with the `format()` function. Figure out using the course manual or documentation how to use this style of string formatting. And a fourth alternative would be to use an f-string. Figure that one out as well.

Also display the types of the results. The first three are of `<class 'int'>`. Notice that the type of the division is `<class 'float'>`.

### Step 3

Now use the `input()` function to ask for the input of two numbers from the user as follows :

```python
s1 = input("give me number 1 : ")
s2 = input("give me number 2 : ")
```

The `input()` function returns a string. Find out about the type of the return values by printing their type. Now perform addition with the `+` operator on the user input. With user input 1 and 3 the result will be 13, because 1 and 3 are seen as strings : the strings are concatenated.

```python
addresult = s1 + s2  # s1='1', s2='3'
print(addresult)     # prints 13
```

Next convert the strings to integers with the `int()` conversion function as follows :

```python
addresult = int(s1) + int(s2)
```

With the same input the result will now be 4. When the given input cannot be converted to an int, a runtime error occurs :

```text
ValueError: invalid literal for int() with base 10: 'w'
```
