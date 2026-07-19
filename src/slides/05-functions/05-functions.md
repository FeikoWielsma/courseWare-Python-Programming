---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Functions
---

# Functions

<!-- NOTES: Perl comparison: 'sub name { my ($a, $b) = @_; ... }' becomes 'def name(a, b): ...'. No @_ array — parameters are named directly. Return is implicit (last expression) or explicit 'return'. Python has no prototypes. Default args: def f(x=10). *args/**kwargs are like Perl's @_ but structured. -->

- A function
  - Python has many built-in functions like `print(),input(),len()` etc.
  - It is also possible to create user-defined functions
- Functions have the following benefits :
  - Modularity of applications and code reuse
- Rules to define a function in Python :
  - Function blocks begin `def` followed by function name and parentheses
  - Any input parameters or arguments should be placed within parentheses
  - It is also possible to define parameters inside these parentheses
- Code block within every function :
  - Starts with a colon (:) and is indented
- Statement `return [expression]` exits a function :
  - Optionally passing back an expression to the caller
  - A return statement with no arguments is the same as return `None`

---

# Function Syntax

- First statement of function can be documentation string of function :
  - docstrings are picked up by documentation tool `pdoc`
  - Installed by `uv add pdoc3` and used with `pdoc --html <module>`

```python
def functionname( parameters ):
    """function_docstring"""
    function_statements
    return [expression]
```

- By default :
  - Parameters have a positional behavior
  - Should pass them in the same order that they were defined
- Example of a simple Python function :
  - Takes a string as input parameter and prints it on standard screen

```python
def showmessage( str ):
    """This prints a passed string into this function"""
    print(str)
```

---

# Calling Functions

- Execute functions by calling them :
  - From another function or directly from the Python prompt
  - If functions specify parameters, it is required to pass them
- Function must be defined before they can be called :
  - Order of definition and call is important
- Example of calling the previously defined `showmessage()` function :

```python
showmessage("First call to user defined function!")
showmessage("Again second call to the same function")
showmessage() # results in error
```

- Result :

```python
First call to user defined function!
Again second call to the same function
Traceback (most recent call last):
  File "01_showmessage.py", line 8, in <module>
```




```python
showmessage()
TypeError: showmessage() takes exactly 1 argument (0 given)
```

> `demo01 · showmessage`


---

# Pass by Value

- Python passes function parameters by value :
  - Parameter in function is copy of variable in caller and refers to same object
  - Change to object via parameter in function is seen by variable in function's caller
  - Mutable and immutable objects behave differently

```python
def changeme( mylist ):
    mylist.append(40)
    print("List inside the function: ", mylist)
    return
```

- Call to `changeme` function :

```python
mylistouter = [10,20,30]
changeme(mylistouter)
print("List outside the function: ", mylistouter)
```

- Reference of passed object is used to append values :

```python
List inside the function changeme1: [10, 20, 30, 40]
```




```python
List outside the function: [10, 20, 30, 40]
```

> `demo02 · passbyvalue`


---

# Overwriting References

- Reference may be overwritten in the function :

```python
def changeme(mylist):
    mylist = [1,2,3,4] # This would assign new reference
    print("Values inside the function: ", mylist)
    return
```

- Call `changeme` function :

```python
mylistouter = [10,20,30]
```




```python
changeme(mylistouter)
print("Values outside the function: ", mylistouter)
```

- Parameter `mylist` is changed in the function `changeme` :
  - Changing `mylist` within the function does not affect `mylistouter`
  - Function does nothing to original list and finally this would produce following result :

```python
Values inside the function: [1, 2, 3, 4]
Values outside the function: [10, 20, 30]
```

- Changing immutable references :

  - Always results in new objects and is true for Strings and Numbers

> `demo03 · overwritingreferences`

> `demo04 · swap`


---

# Function Arguments

- Functions can be called with different types of arguments
- Required arguments :
  - Passed to a function in correct positional order
  - Number of arguments in call should match exactly with the definition
- Keyword arguments :
  - Caller identifies arguments by name and allows parameters to be out of order
  - Python interpreter is able to use the keywords to match the values with parameters
- Default arguments :
  - Assume default value if value is not provided in the function call for that argument
- Variable-length arguments :
  - Sometimes more arguments must be processed than specified in function definition
  - These are called variable-length arguments and are not named in function definition
- Python does not support function overloading :


  - Defining same method with different parameters
  - Python is dynamically typed and supports optional arguments

> `demo05 · power1`

---

# Keyword Arguments

- Function definition :

```python
def printinfo(name, age):
    """This prints name and age passed into this function"""
    print("Name: ", name)
    print("Age: ", age)
    return
```

- Function call with keyword arguments :

```python
printinfo(age=55, name= "Albert")
```

- Result :

```python
Name: Albert
Age: 55
```

- Calling code specifies arguments by name :
  - Parameters do not have to follow the order in the function definition

> `demo06 · keywordarguments`


---

# Default Arguments

- Function definition :

```python
def printinfo(name, age = 35):
     """This prints name and age passed into this function"""
     print("Name: ", name)
     print("Age: ", age)
     return
```

- Functions calls with and without default arguments :

```python
printinfo(age=55, name= "Albert")
printinfo(name= "Werner")
```

- Results :

```python
Name: Albert
Age: 55
Name: Werner
Age: 35
```

> `demo07 · defaultarguments`


---

# Variable Length Arguments

- Syntax for function with variable arguments :

```python
def testArgLists(arg, *argtuple, **kwargs):
     """Function referencing argument, argument list and keyword arguments"""
     print('arg:', arg)
     print('args:', argtuple)
     print('kwargs:', kwargs)
```

- `*args_tuple :`
  - Asterisk (*) indicates variable holding values of all non-keyword variable arguments
  - Tuple remains empty if no additional arguments are specified during function call
- `**args_keywords :`
  - Double asterisk (**) indicates a variable-length argument list with keywords
  - Dictionary remains empty if no keyword arguments are passed

```python
testArgLists(1, 2, 3, 4, 5, x=1, y=2)
testArgLists(33, x=8, y=9)
```




```python
testArgLists(44)08_variable_argumentlist
```

> `demo08 · variableargumentlist`


---

# Anonymous Functions

- `lambda` keyword is used to create small anonymous functions :
  - Not declared in the standard manner by using the `def` keyword
- Lambda form can take any number of arguments :
  - Return just one value in the form of an expression
  - Cannot contain commands or multiple expressions
- Characteristics of lambda functions :
  - Have their own local namespace
  - Cannot access variables besides in parameter list and in global namespace
  - Cannot be a direct call to print because lambda requires an expression
  - Can be stored in variables and passed and returned to functions
- Lambda's appear to be a one-line versions of a function :
  - However they are not equivalent to inline statements in C or C++

---

# Syntax Lambda Functions

- Lambda functions contain only a single statement :

```python
lambda [arg1 [,arg2,.....argn]]:expression
```

- Function definition :

```python
summation = lambda arg1, arg2: arg1 + arg2
```

- Function call :

```python
print("Value of total : ", summation( 10, 20 ))
print("Value of total : ", summation( 20, 20 ))
```

- Result :

```python
Value of total : 30
Value of total : 40
```

> `demo09 · lambdafunctions`


---

# return Statement

- `return [expression]` exits a function :
  - Optionally passing back an expression to the caller
  - `return` statement with no arguments is the same as return `None`
  - `return` statement is not required and then default return value is `None`
- Function definition :

```python
def summation(arg1, arg2):
    """Add both the parameters and return them"""
    tot = arg1 + arg2
    print("Inside the function : ", tot)
    return tot
```

- Function call :

```python
total = summation(10, 20)
print("Outside the function : ", total )
```

- Result :



```python
Inside the function : 30
Outside the function : 30
```

> `demo10 · returnstatement`

---

# Scope of Variables

- Accessibility of variable depends on where it is declared :
  - Scope determines where in program you can access a particular identifier
- There are two basic scopes of variables in Python :
  - Global variables
  - Local variables
- Global versus Local variables :
  - Variables defined inside a function body have a local scope
  - Variables defined outside have a global scope
- Local variables :
  - Can be accessed only inside the function in which they are declared
  - When you call a function, the variables declared inside it are brought into scope
- Global variables :
  - Can be accessed throughout the program body by all functions
  - Refer to global instead of a local variable inside function with `global` keyword

---

# Example Variable Scope


```python
x = 50 # This is a global variable
y = 50 # This is a global variable
```

- Function definitions :

```python
def func1():
     x = 2
     print ('Changed local x to', x) # prints 2
def func2():
     print('Access global x as', x)
def func3():
    global y
    y = 2
    print ('Changed global y to', y) # prints 2
```

- Function calls :

```python
func1() # prints 2
print('x is still', x) # prints 50
func2() # prints 50
```




```python
print('x is still', x) # prints 50
func3() # prints 2
print('Value of y is', y) # prints 2
```

> `demo11 · variablescope`

---

# Summary : Functions

- Functions are blocks of reusable code performing some action :
  - Python has built-in functions and it is possible to create user-defined functions
- Python functions are defined with the `def` statement :
  - They can accept parameters, have a code block and a return statement
- Python passes function parameters by value :
  - Parameter in function refers to same object as in caller
- Functions can be called with different types of arguments :
  - Required, Keyword, Default and Variable-length arguments
- `lambda` keyword is used to create small anonymous functions :
  - Return value as an expression, cannot contain commands or multiple expressions
- Local variables :
  - Variables defined inside a function body have a local scope
- Global variables :Exercise 5
  - Variables defined outside functions have a global scope
