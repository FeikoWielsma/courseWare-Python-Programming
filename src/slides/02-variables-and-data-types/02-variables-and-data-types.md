---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Variables and Data Types
---

# Variables

- Variables are names bound to objects :
  - Assignment binds a name to the object produced by an expression
  - Several names can refer to the same object
- Objects have types, such as `int`, `float` and `str` :
  - `type(x)` returns the type of the object currently bound to `x`
  - Rebinding `x` can make it refer to an object of a different type
- `id(x)` identifies the object while it exists
- The `=` operator binds the name on its left to the object on its right :
  - A name does not need a separate declaration before assignment

```python
counter = 100  # An integer assignment
miles = 1000.0  # A floating point
name = "John"  # A string
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
  - This is known as aliasing
- Variable names are not properties of an object :
  - A namespace maps each name to the object it refers to

<svg viewBox="0 0 960 190" width="100%" style="width:100%;height:auto;display:block;margin:8px 0 4px" role="img" aria-label="Two names in a namespace refer to one object, which carries the identity, type and value">
<defs>
<marker id="nb-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<g fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.5">
<rect x="20" y="30" width="250" height="130" rx="4"/>
</g>
<g fill="currentColor" font-size="17" opacity="0.75">
<text x="30" y="22">namespace</text>
<text x="560" y="22">one object</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="50" y="52" width="120" height="38" rx="3"/>
<rect x="50" y="106" width="120" height="38" rx="3"/>
<rect x="540" y="40" width="360" height="112" rx="4"/>
</g>
<g fill="currentColor" font-size="21" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" text-anchor="middle">
<text x="110" y="78">a</text>
<text x="110" y="132">b</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#nb-arrow)">
<path d="M 170 71 L 350 71 L 350 96 L 534 96"/>
<path d="M 170 125 L 350 125 L 350 96 L 534 96"/>
</g>
<g fill="currentColor" font-size="20" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
<text x="562" y="70">id(x)   140237... </text>
<text x="562" y="102">type(x) int</text>
<text x="562" y="134">value   5</text>
</g>
<g fill="currentColor" font-size="17" opacity="0.75" text-anchor="middle">
<text x="352" y="172">a is b, and id(a) == id(b)</text>
</g>
</svg>

> `demo02 · typeandid`


---

# Multiple Assignment

- Simultaneous assignment of values :

```python
a = b = c = 1
```

- All three names are bound to the same integer object
- Reassigning one name changes only that binding :
  - The other names still refer to the original object
- Integers are immutable :
  - Rebinding a name does not change the integer it previously named
  - The new binding may refer to an already existing object
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
  - An operation the type does not allow raises rather than coercing silently

```text
1 + 1      ->  2             int plus int
"1" + "1"  ->  '11'          str plus str, concatenation
"1" + 1    ->  TypeError     no implicit conversion between the two
```

- Important Python data types :
  - Numbers, String, List, Tuple, Set and Dictionary

> `demo04 · strongtyping`


---

# Annotating Variables

- A variable can carry a type hint saying what it is meant to hold :

```python
age: int = 25
height: float = 1.87
name: str = "Alice"
is_student: bool = True
```

- The hint changes nothing at runtime :
  - Python still stores whatever it is given, and still checks types only when
    an operation is attempted
  - The annotation records the intent, so that a reader and a tool can see it
- It is worth writing where the type is not obvious from the value :
  - `total: float = 0` says that the running total will not stay an integer
  - An editor can then complete and check against the annotation
- Annotations appear throughout the rest of this course :
  - Collections in the data structures module, functions in the functions module
  - The appendix gathers them up and adds a checker


---

# Python Numbers

- Assignment binds names to number objects :

```python
var1 = 1
var2 = 10
```

- Numbers are immutable data types :
  - Reassignment binds a name to another number; it does not modify the old one

```python
var1 = 11
var1 = 2
var2 = 1
```

- Remove one or more name bindings with `del`; other references keep the objects alive :

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
y2 = repr("abc")  # y2 is "'abc'"
y3 = str("abc")   # y3 is 'abc'
i = 65
print(chr(i))    # A
print(hex(i))    # 0x41
print(ord("A"))  # 65
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
| `sqrt(x)` | The square root of x, for x >= 0 |
| `max(x, y, ..)` / `min(x, y, ..)` | The maximum or minimum of a list of numbers |

- For some of these functions the `math` module must be imported

> `demo07 · numberfunctions`

---

# Python Operators

- An operator combines one or more operands into a new value :

```python
print(7 / 2)  # 3.5, true division always gives a float
print(7 // 2)  # 3, floor division drops the fraction
print(7 % 2)  # 1, the remainder
print(2**10)  # 1024, exponentiation
```

- Python groups its operators as follows :
  - Arithmetic and assignment operators, for numbers and for strings
  - Comparison operators, which give `True` or `False`
  - Logical, membership and identity operators
- Bitwise operators `& | ^ ~ << >>` work on the bits of integers, rarely needed
- There is no `++` or `--` : write `count += 1` instead

> `demo08 · pythonoperators`

---

# Arithmetic and Assignment Operators

| Operator | Arithmetic Operator Description |
|---|---|
| `+` / `-` | Adds or subtracts the values on either side of the operator |
| `*` | Multiplies the values on either side of the operator |
| `/` | Divides left operand by right operand, the result is always a float |
| `//` | Floor division, the quotient rounded down to a whole number |
| `%` | Modulo, the remainder of the division |
| `**` | Exponentiation, the left operand raised to the power of the right |

| Operator | Assignment Operator Description |
|---|---|
| `=` | Binds the name on the left to the value on the right |
| `+=` / `-=` | Adds or subtracts the right operand, and assigns the result to the left |
| `*=` / `/=` | Multiplies or divides by the right operand, and assigns the result |
| `//=` / `%=` / `**=` | The same for floor division, modulo and exponentiation |

```python
count = 10
count += 1
count *= 2
print(count)  # 22
```

---

# Comparison Operators

| Operator | Comparison Operator Description |
|---|---|
| `==` / `!=` | True if the two values are equal, or not equal |
| `>` / `<` | True if the left value is greater, or less, than the right |
| `>=` / `<=` | True if the left value is greater or equal, or less or equal |

- Comparisons chain, so a range check reads as it would on paper :

```python
i = 10
j = 11
print(i > j)  # False
print(i != j)  # True
print(0 < i < 20)  # True, comparisons chain
print("apple" < "banana")  # True, strings compare letter by letter
```

- `==` compares values; whether two names are one object is `is`, on the next slide

---

# Logical, Membership, Identity Operators

| Operator | Description |
|---|---|
| `and` / `or` | True if both operands are true, or if at least one is |
| `not` | Reverses the truth value of its operand |
| `in` / `not in` | True if the value is, or is not, an element of the sequence |
| `is` / `is not` | True if both sides are, or are not, the very same object |

- `and` and `or` stop as soon as the answer is known, and return an operand :

```python
name = ""
print(name or "anonymous")  # anonymous, `or` returns the first truthy operand
```

- `is` asks whether two names refer to one object, `==` whether values are equal :

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c)  # True, equal values
print(a is c)  # False, two different lists
print(a is b)  # True, two names for one list
```

> `demo09 · booleanoperators`

---

# Python Operators Precedence

| Operator | Description, from highest to lowest |
|---|---|
| `**` | Exponentiation, which groups from the right |
| `+x` `-x` `~x` | Unary plus, minus and bitwise not |
| `*` `/` `//` `%` | Multiplication, division, floor division and modulo |
| `+` `-` | Addition and subtraction |
| `<<` `>>` `&` `^` `\|` | Bitwise shifts, and, exclusive or, or |
| `==` `!=` `<` `<=` `>` `>=` `in` `not in` `is` `is not` | Comparisons, membership and identity |
| `not` | Logical not |
| `and` | Logical and |
| `or` | Logical or |

```python
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
print(2**3**2)  # 512, ** groups from the right
```

- When in doubt, add parentheses : they cost nothing and help the reader

---

# Python Strings

- Strings are sequences of characters between quotation marks :
  - Pairs of single `'` quotes, of double `"` quotes and of triple (''' or """) quotes supported
  - There is no distinction between single and double quoted strings
- Creating strings is as simple as assigning a value to a variable :

```python
var1 = "Hello World!"
var2 = "Python Programming"
```

- Python does not support a character type :
  - Characters are treated as strings of length one, thus also considered a substring
  - To access substrings, use square brackets for slicing along with the index

```python
print("var2[1:5]:", var2[1:5])
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

---

# String Operations

- Examples :

```python
print(str1)  # Prints complete string
print(str1[0])  # Prints first character of the string
print(str1[-1])  # Prints last character of the string
print(str1[2:5])  # Prints characters starting from 3rd through 5th
print(str1 * 2)  # Prints string two times
print(str1 + "TEST")  # Prints concatenated string
print(str1[::-1])  # Prints string backwards
```

- String updated by assigning part of it to new string :
  - New value can be related to its previous value or to a completely different string

```python
var1 = "Hello World!"
var2 = var1[:6] + "Python"
print("Updated String :-", var2)
```

- Result :



```text
Updated String :- Hello Python
```
- New string var2 will have different id

> `demo10 · stringoperations`

---

# Escape Characters

- Escape or non-printable characters :
  - Characters that can be represented with backslash notation

| Backslash Notation | Hexadecimal Character | Description |
|---|---|---|
| `\` | 0x5c | Backslash |
| `\'` / `\"` | 0x27 / 0x22 | Single or double quote |
| `\n` | 0x0a | Newline |
| `\r` | 0x0d | Carriage return |
| `\t` | 0x09 | Tab |
| `\a` | 0x07 | Bell or alert |
| `\b` | 0x08 | Backspace |
| `\ooo` | | Character with octal value ooo, digits 0 to 7 |
| `\xhh` | | Character with hexadecimal value hh |
| `\uxxxx` | | Unicode character with 16-bit hexadecimal value xxxx |

> `demo11 · escapecharacters`

---

# Raw and Unicode Strings

- Raw String don't treat backslash as a special character :
  - Every character in a raw string stays the way it was
- In a normal String the backslash can be escaped :

```python
print("C:\\nowhere")
```

- Result : `C:\nowhere`
- A raw string is made with the `r` in front of the String :

```python
print(r"C:\nowhere")
```

- Result : `C:\nowhere`
- Python strings are Unicode :
  - A string is a sequence of code points, so `len("Ä…Ä‡")` is 2
  - Text in almost every script in the world can be stored and processed
- `unicodedata` module `:`
  - Provides access to Unicode Character Database (UCD)
  - UCD contains character properties for all Unicode characters


---

# f-Strings

- An f-string is a string literal with an `f` in front of the opening quote :
  - Each `{expression}` inside it is evaluated, and its value takes its place
  - Any expression works, including arithmetic and method calls

```python
name = "Albert"
age = 55
print(f"My name is {name} and my age is {age}")
print(f"{name.upper()} will be {age + 1} next year")
```

```text
My name is Albert and my age is 55
ALBERT will be 56 next year
```

- Two markers after the expression change what is shown :
  - `!r` shows the value as `repr()` does, a string with its quotes
  - `=` shows the expression as well as its value, which helps when debugging

```python
print(f"{name!r}")  # 'Albert', the repr() with its quotes
print(f"{age = }")  # age = 55, the expression and its value
```

> `demo12 · f-strings`

---

# Format Specifications

- A colon after the expression starts a format specification :

<svg viewBox="0 0 960 240" width="100%" style="width:100%;height:auto;display:block;margin:10px 0 6px" role="img" aria-label="Each replacement field of the f-string renders its expression with its format specification into the result string">
<g fill="currentColor" font-size="17" opacity="0.75" text-anchor="middle">
<text x="152" y="52">art is 453</text>
<text x="488" y="52">price is 59.058</text>
</g>
<g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="21" fill="currentColor">
<text x="20" y="92" textLength="72" lengthAdjust="spacingAndGlyphs">f"Art:</text>
<text x="104" y="92" textLength="96" lengthAdjust="spacingAndGlyphs">{art:5d}</text>
<text x="200" y="92" textLength="204" lengthAdjust="spacingAndGlyphs">, Price per Unit:</text>
<text x="416" y="92" textLength="144" lengthAdjust="spacingAndGlyphs">{price:8.2f}</text>
<text x="560" y="92" textLength="12" lengthAdjust="spacingAndGlyphs">"</text>
</g>
<g fill="none" stroke="currentColor" stroke-width="2">
<rect x="102" y="72" width="100" height="28" rx="3"/>
<rect x="414" y="72" width="148" height="28" rx="3"/>
</g>
<defs>
<marker id="fs-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<g fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#fs-arrow)">
<path d="M 152 100 L 152 140 L 110 140 L 110 186"/>
<path d="M 488 100 L 488 140 L 404 140 L 404 186"/>
</g>
<g fill="currentColor" opacity="0.12">
<rect x="80" y="188" width="60" height="38"/>
<rect x="356" y="188" width="96" height="38"/>
</g>
<g fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.5">
<rect x="20" y="188" width="432" height="38"/>
</g>
<g font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="21" fill="currentColor">
<text x="20" y="214" textLength="48" lengthAdjust="spacingAndGlyphs">Art:</text>
<text x="140" y="214" textLength="36" lengthAdjust="spacingAndGlyphs" text-anchor="end">453</text>
<text x="140" y="214" textLength="204" lengthAdjust="spacingAndGlyphs">, Price per Unit:</text>
<text x="452" y="214" textLength="60" lengthAdjust="spacingAndGlyphs" text-anchor="end">59.06</text>
</g>
<g fill="currentColor" font-size="17" opacity="0.75">
<text x="600" y="124">5d : an integer, 5 wide</text>
<text x="600" y="152">8.2f : a float, 8 wide, 2 decimals</text>
<text x="480" y="214">result string</text>
</g>
</svg>

- The specification sets the width, the alignment and the decimals :

```python
print(f"[{'Curie':<10}]")  # [Curie     ]
print(f"[{'Curie':^10}]")  # [  Curie   ]
print(f"[{'Curie':>10}]")  # [     Curie]
print(f"{1234567.891:,.2f}")  # 1,234,567.89
print(f"{0.25:.0%}")  # 25%
```

- Older code formats the same way with `%` or `str.format`, recognise them :

```python
print("Art: %5d, Price per Unit: %8.2f" % (art, price))
print("Art: {:5d}, Price per Unit: {:8.2f}".format(art, price))
```

> `demo13 · formatspecs`

---

# Triple Quotes

- Allow strings to span multiple lines :
  - Including verbatim NEWLINEs, TABs, and any other special characters
- Syntax consists of three consecutive single or double quotes :

```python
para_str = """this string is made up of several lines and non-printable
characters such as TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like this within the
brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up."""
print(para_str)
```

- Result :

```text
this string is made up of several lines and non-printable
characters such as TAB (         ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like this within the
brackets [
 ], or just a NEWLINE within
the variable assignment will also show up.
```

> `demo14 · triplequotes`


---

# Built-in String Methods

- String methods are called with dot notation : `"albert".upper()`
  - A string never changes, so each method returns a new string or a value

| Method | Description |
|---|---|
| `strip()` | Removes whitespace from both ends, `lstrip()` and `rstrip()` from one |
| `lower()` / `upper()` | Converts the string to all lowercase or all uppercase |
| `split(sep)` | Splits the string into a list of words, on whitespace by default |
| `sep.join(words)` | Joins a list of strings into one, with `sep` between them |
| `count(sub)` | Returns how many times `sub` occurs in the string |
| `startswith(prefix)` | Returns `True` if the string starts with `prefix`, see also `endswith()` |
| `isalpha()` | Returns `True` if the string is not empty and holds only letters |
| `replace(old, new)` | Returns a copy with every `old` replaced by `new` |
| `find(sub)` | Returns the index of the first `sub`, or `-1` if it is not there |

- `len(s)` is a function rather than a method, and gives the number of characters
- All the others : `https://docs.python.org/3/library/stdtypes.html#string-methods`

> `demo15 · stringfunctions`

---

# Summary : Variables and Data Types

- A variable is a name bound to an object :
  - Created on first assignment with `=`, and can be annotated, as in `age: int = 25`
  - Every object has an identity, `id(x)`, a type, `type(x)`, and a value
- Python is strongly typed :
  - Converting between types is explicit, with `int()`, `float()`, `str()` and `bool()`
- Numbers are `int`, `float` and `complex`; `bool` is a subtype of `int`
- Operators compute, compare and combine values :
  - `==` compares values, `is` compares identities
- Strings are immutable sequences of Unicode characters :
  - Indexed and sliced with `[]`, and have methods such as `strip()` and `split()`
- f-strings are the way to format text :
  - `f"{price:8.2f}"` sets the width and the decimals of the value it shows

> `exercise02 · Variables and Data Types`
