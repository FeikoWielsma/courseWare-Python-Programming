---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Variables and Data Types
---

# Variables

<!-- NOTES: Perl comparison: 'my $x = 5' becomes 'x = 5'. No sigils, no 'my'. Python is dynamically typed like Perl, but variable names are bare identifiers. Type hints (x: int = 5) are optional annotations, not enforced at runtime. -->

- Variables are
  - When a variable is created memory space is reserved
- Variables can have different data types like integers, decimal or string :
  - Based on the data type of a variable, the interpreter allocates memory
  - Type of the variable can change and is found with `type` function
- Variable `x` represents an object :
  - Unique identifier of an object is an integer and is returned by `id(x)`
- Assigning values to variables :
  - Variables do not have to be declared; declaration happens on first assignment
- Equal sign `=` is used to assign values to variables :
  - Operand to the left of the = operator is the name of the variable
  - Operand to the right of the = operator is the value stored in the variable

```python
counter = 100 # An integer assignment
miles = 1000.0 # A floating point
name = "John" # A string
```
- Python language does not have constants

> `demo01 · variables`

---

# Everything is an Object

- Each object `x` has :
  - Unique identifier, an integer, returned by `id(x);`
  - Type returned by `type(x)`
  - Value may or may not be changeable :
    - Value can itself consist of one or more objects
  - Zero or more methods provided by type object to get and/or change content
  - Zero or more names
- Objects have individuality :
  - Multiple names in multiple scopes can be bound to the same object
  - This is known as aliasing in other languages
- Variable names are not properties of an object :
  - They are stored in separate namespaces
  - Dictionaries of name → object reference (id) pairs

> `demo02 · typeandid`


---

# Multiple Assignment

- Simultaneous assignment of values :

```python
a = b = c = 1
```

- Integer object is created with value 1 :
  - All three variables are assigned to the same memory location
- As soon as one variable changes new object is created :
  - Changed variable points to this new object
- In fact once Integer object with value is created :
  - Value is a constant object that cannot be changed
  - Change leads to the creation of a new object
- Assignment of multiple objects to multiple variables :

```python
a, b, c = 1, 2, "john"
```

- Two integer objects with values 1 and 2 :
  - Assigned to variables a and b


- One string object with the value "john" :

  - Assigned to the variable c

> `demo03 · multipleassignment`


---

# Strong Typing

- Data stored in memory can be of many types :
  - Persons age is stored as a numeric value
  - Persons address is stored as alphanumeric characters
- A type (or class) of a variable determines :
  - Operations possible on the variable
  - Storage method for the variable
- Python is a strongly typed language :
  - Trying to perform operations on a type that are not allowed gives error
- Important Python data types :
  - Numbers
  - String
  - List
  - Tuple


  - Set

  - Dictionary

> `demo04 · strongtyping`


---

# Python Numbers

- Number objects are created when you assign a value to them :

```python
var1 = 1
var2 = 10
```

- Numbers are immutable data types :
  - Changing the value of a number data type results in a newly allocated object

```python
var1 = 11
var1 = 2
var2 = 1
```

- Delete single object or multiple objects with `del` statement :

```python
del var
del var_a, var_b
```

---

# Type Conversions

- Sometimes number must be explicitly converted :
  - Coerced from one type to another to satisfy requirements of function parameter
- Built-in functions perform conversion between data types :
  - `int(x [,base]) :`
    - Converts x to a plain integer, base specifies the base if x is a string
  - `float(x) :`
    - Converts x to a floating-point number
  - `bool([x])` :
    - Convert value to Boolean using standard truth testing procedure
- All integers, positive and negative behave as `True` :
  - Only 0 behaves as `False`
- All non empty strings behave as `True` :
  - Only empty string `""` behave as `False` and `None` as well


- Boolean type is a subtype of the integer type :

  - Boolean values behave like values 0 and 1
  - When converted to a string in string context `"False"` or `"True"` are returned

> `demo05 · numbertypeconversion`


---

# Conversion Functions

- Functions to convert between built-in types :

| Function | Description |
|---|---|
| `str(x)` | Converts object x to a string representation |
| `repr(x)` | Converts object x to an expression string |
| `eval(expression)` | Evaluates a Python expression and returns result |
| `chr(x)` | Converts an integer Unicode codepoint to a character |
| `ord(x)` | Converts character to integer representing Unicode code point |
| `hex(x)` | Converts an integer to a hexadecimal string |
| `oct(x)` | Converts an integer to an octal string |

```python
y2 = repr('abc')   # y2 is "'abc'"
y3 = str('abc')    # y3 is 'abc'
i = 65
print (chr(i))     # A
print (hex(i))     # 0x41
print (ord('A'))   # 65
```

> `demo06 · conversionfunctions`

---

# Built-in Number Functions

| Function | Description |
|---|---|
| `abs(x)` | Absolute value of x: the (positive) distance between x and zero |
| `ceil(x)` | The ceiling of x: the smallest integer greater than or equal to x |
| `exp(x)` | The exponential of x: e**x |
| `fabs(x)` | The absolute value of x, is part of math module |
| `floor(x)` | The floor of x: the largest integer not greater than x |
| `log(x)` | The natural logarithm of x, for x > 0 |
| `log10(x)` | The base-10 logarithm of x, for x > 0 |
| `pow(x, y)` | The value of x**y |
| `sqrt(x)` | The square root of x, for x > 0 |
| `max(x, y, ..)` / `min(x, y, ..)` | The maximum or minimum of a list of numbers |

- For some of these functions the `math` module must be imported

> `demo07 · numberfunctions`

---

# Python Strings

- Strings are sets of characters between quotation marks :
  - Pairs of single `'` quotes, of double `"` quotes and of triple (''' or """) quotes supported
  - There is no distinction between single and double quoted strings
- Creating strings is as simple as assigning a value to a variable :

```python
var1 = 'Hello World!'
var2 = "Python Programming"
```

- Python does not support a character type :
  - Characters are treated as strings of length one, thus also considered a substring
  - To access substrings, use square brackets for slicing along with the index

```python
print ("var2[1:5]: ", var2[1:5])
```

  - Indexes start at 0 in beginning of the string, then upwards and to -1 at the end
- Strings are immutable data types like Numbers :
  - Changing the value of a string data type results in a newly allocated object

---

# String Operators

| Operator | Description |
|---|---|
| `+` | Concatenation. Adds values on either side of the operator |
| `*` | Repetition. Creates string by concatenating multiple copies of same string |
| `[]` | Slice. Gives the character from the given index |
| `[:]` | Range Slice. Gives the characters from the given range |
| `in` | Membership. Returns true if a character exists in the given string |
| `not in` | Membership. Returns true if a character does not exist in the given string |
| `r/R` | Raw String. Suppresses actual meaning of escape characters |
| `%` | Format. Performs string formatting |

---

# String Operations

- Examples :

```python
print(str1) # Prints complete string
print(str1[0]) # Prints first character of the string
print(str1[-1]) # Prints last character of the string
print(str1[2:5]) # Prints characters starting from 3rd to 6th
print(str1 * 2) # Prints string two times
print(str1 + "TEST") # Prints concatenated string
print(str1[::-1]) # Prints string backwards
```

- String updated by assigning part of it to new string :
  - New value can be related to its previous value or to a completely different string

```python
var1 = 'Hello World!'
var2 = var1[:6] + 'Python'
print("Updated String :- ", var2)
```

- Result :



```python
Updated String :- Hello Python
```
- New string var2 will have different id

> `demo08 · stringoperations`

---

# Escape Characters

- Escape or non-printable characters :
  - Characters that can be represented with backslash notation

| Backslash Character | Hexadecimal Character | Description |
|---|---|---|
| `\a` | 0x07 | Bell or alert |
| `\b` | 0x08 | Backspace |
| `\e` | 0x1b | Escape |
| `\f` | 0x0c | Formfeed |
| `\n` | 0x0a | Newline |
| `\nnn` | | Octal notation, n in range from 0-7 |
| `\r` | 0x0d | Carriage return |
| `\s` | 0x20 | Space |
| `\t` | 0x09 | Tab |
| `\v` | 0x0b | Vertical Tab |

> `demo09 · escapecharacters`

---

# Raw and Unicode Strings

- Raw String don't treat backslash as a special character :
  - Every character in a raw string stays the way it was
- In a normal String the backslash can be escaped :

```python
print ('C:\\nowhere')
```

- Result : `C:\nowhere`
- A raw string is made with the `r` in front of the String :

```python
print (r'C:\\nowhere')
```

- Result : `C:\\nowhere`
- Since Python 3 all strings are stored as Unicode internally :
  - In Unicode strings consist of (32-bit) code points
  - Allows more characters, including characters from most languages in the world
- `unicodedata` module `:`
  - Provides access to Unicode Character Database (UCD)

  - UCD contains character properties for all Unicode characters


---

# String Formatting

- String formatting has seen a lot of changes between Python versions :
  - Earlier version used string formatting using format specifiers like in C
  - Also available came the `format` method to implement string formatting
  - Latest Python versions support `f` strings with variable interpolation like in PHP
- Operator `%` is string format operator an is unique to strings :
  - Used in Pythons version of C's `printf()` function

```python
print ("My name is %s and weight is %d kg!" % ('Albert', 55))
```

  - Result : `My name is Albert and weight is 55 kg!`
- In Python 3 new style of formatting available with `format()` function :
  - Allows complex variable substitutions and value formatting

```python
s = '{0}, {1}, {2}'.format('a', 'b', 'c')
print (s) => 'a, b, c'
s = '{}, {}, {}'.format('a', 'b', 'c')
print (s) => 'a, b, c'
```




```python
s = '{2}, {1}, {0}'.format('a', 'b', 'c')
print (s) => 'c, b, a'
```

> `demo10 · stringformatting`

---

# String Format Symbols

| Symbol | Functionality |
|---|---|
| `%s` | String conversion via `str()` prior to formatting |
| `%i` / `%d` | Signed decimal integer |
| `%o` | Octal integer |
| `%x` | Hexadecimal integer |
| `%f` | Floating point real number |
| `*` | Argument specifies width or precision |
| `-` | Left justification |
| `+` | Display the sign |
| `#` | Add the octal leading zero or hexadecimal leading 0x or 0X |
| `0` | Pad from left with zeros instead of spaces |
| `%%` | Leaves you with a single literal % |
| `m.n.` | m is minimum total width, n is nr. of digits after decimal point |

---

# Format Method

> `demo11 · formatmethod`


---

# f Strings

- As of Python 3.6 f-strings are great new way to format strings :
  - They more readable, faster, more concise and less prone to error than other formatting ways
- f-strings are string literals that have an `f` at the beginning :
  - Inside there are curly braces containing expressions that will be replaced with their values
  - Expressions are evaluated at runtime and then formatted using the `__format__` protocol
- Syntax is similar to the one used with `str.format()` but less verbose :

```python
name = "Albert"
age = 55
print(f"My name is {name} and my age is {age}")
```

- f-strings are evaluated at runtime, can put valid Python expressions in them :
  - And can also call methods

```python
name = "Enrico Fermi"
f"{name.upper()} is the creator of the first fission reactor"
f"{name.upper():40} is the creator of the first fission reactor"
```

> `demo12 · f-strings`


---

# Triple Quotes

- Allow strings to span multiple lines :
  - Including verbatim NEWLINEs, TABs, and any other special characters
- Syntax consists of three consecutive single or double quotes :

```python
para_str = """this string is made up of several lines and non-printable
   characters such as TAB ( \t ) and they will show up that way when displayed.
   NEWLINEs within the string, whether explicitly given like this within the
   brackets [ \n ], or just a NEWLINE
    within the variable assignment will also show up."""
print (para_str)
```

- Result :

```python
this string is made up of several lines and non-printable
characters such as TAB ( ) and they will show up that way when
displayed. NEWLINEs within the string, whether explicitly given like
this within the brackets [
 ], or just a NEWLINE
within the variable assignment will also show up.
```

> `demo13 · triplequotes`


---

# Built-in String Functions

| Function | Description |
|---|---|
| `capitalize()` | Capitalizes first letter of string |
| `isdigit()` | Returns true if string contains only digits and false otherwise |
| `isnumeric()` | Returns true if string has only numeric characters, false otherwise |
| `len(string)` | Returns the length of the string |
| `lower()` / `upper()` | Converts string to all lowercase or all uppercase |
| `lstrip()` / `rstrip()` | Removes leading or trailing whitespace in string |
| `maketrans()` | Returns a translation table to be used in translate function |
| `max(str)` / `min(str)` | Returns the max or min alphabetical character from the string |
| `swapcase()` | Inverts case for all letters in string |
| `strip([chars])` | Performs both lstrip() and rstrip() on string |

- Most functions are members of the `String` class :
  - Must be called using dot notation : `"albert".upper()`

> `demo14 · stringfunctions`

---

# Summary : Variables and Data Types

- Variables represent memory locations to store values :
  - When a variable is created memory space is reserved
- Assigning Values to Variables :
  - Python variables do not have to be explicitly declared to reserve memory space
- Equal sign `=` is used to assign values to variables :
  - Operand to the left of the = operator is the name of the variable
- Python has five standard data types :
  - Numbers, String, List, Tuple, Dictionary
- Python supports different types to store numeric values :
  - `int` , `float, complex`
- Python boolean type is a subtype of integer :
  - Only allowed values are 0 and 1 printed as `"True"` and `"False"`
- Python has built-in functions to convert between data types :
  - Functions return new object representing converted valueExercise 2
