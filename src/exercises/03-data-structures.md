# Exercise 3 : Data Structures

In this exercise you extend the calculator with lists, multidimensional lists, tuples and dictionaries.

---

### Step 1

Create a project or directory named `exercise3` and a Python module `calculator3.py`. Next create an empty list variable and ask the user for the input of two float numbers. Add these numbers, store the result in a variable and append the numbers and the result of their addition to the list. Repeat this operation until the user quits the program by pressing the red button in the IDE. Your code could look like the following :

```python
reslist = []
while True:
    f1 = float(input("Give me number 1 : "))
    f2 = float(input("Give me number 2 : "))
    addresult = f1 + f2
    reslist.append(f1)
    reslist.append(f2)
    reslist.append(addresult)
```

Also print the content of the list, print the length of the list and print a subset of the list as follows :

```python
print (f"Content of list : {reslist}")
print (f"Length of list : {len(reslist)}")
print (f"Part of list : {reslist[0:3]}")
```

Finally remove the first element of the list and print the list again :

```python
print (reslist[0])
del reslist[0]
print (f"Content of list after deletion : {reslist}")
```

### Step 2

Now create a multidimensional list in which each row contains a calculation with as elements the type of operation, the two float numbers and the result. Also calculate the results of the subtraction, multiplication and division and store these as rows in the multidimensional list. Start by allocating memory for the multidimensional list as follows :

```python
multireslist = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
```

Then store the results of the operations in separate lists and add these lists at appropriate places in the multidimensional list. For the add operation your code could look as follows :

```python
addresult = f1 + f2
addlist = ["Add", f1, f2, addresult]
multireslist[0] = addlist
```

Write similar code for the subtract, multiply and divide operations. Print the multidimensional list after storing the results. Your result should look as follows :

```text
Content of list : [['Add', 2.0, 2.0, 4.0], ['Subtract', 2.0, 2.0, 0.0],
['Multiply', 2.0, 2.0, 4.0], ['Divide', 2.0, 2.0, 1.0]]
```

Finally try to change some element in one of the sublists and notice that you are able to make the change. Then change one of the sublists to a tuple :

```python
addlist = ("Add", f1, f2, addresult)
```

Notice that when you try to change elements of this tuple you get the following error :

```text
TypeError: 'tuple' object does not support item assignment
```

### Step 3

Now create an empty dictionary. Ask the user for the input of two numbers like before. Perform add, subtract, multiply and divide operations on the numbers. Store the numbers and the results of the calculation in a small list for each calculation type :

```python
resdict = {}
while True:
    f1 = float(input("Give me number 1 : "))
    f2 = float(input("Give me number 2 : "))
    addresult = f1 + f2
    addlist = [f1, f2, addresult]
```

Now store the list in the dictionary under the key `"Add"` as follows :

```python
resdict["Add"] = addlist
```

Use similar code for the other calculation operations and print the dictionary after the input of two numbers.

Try to read and extend the value at a dictionary key. The reading will succeed if the dictionary key was created before, but you will get an error if the key did not exist. Next make sure that the keys exist before starting to ask input from the user, by initializing the dictionary as follows :

```python
resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
```

Now store multiple results of add calculations under the `"Add"` key as follows :

```python
resdict["Add"] = resdict["Add"] + addlist
```

### Step 4

Ask the user to input a list of integers and split the input string into a list :

```python
s = input("Give me a set of numbers separated by space characters : ")
slist = s.split(' ')
print (slist)
```

Also sort and reverse the list with the `sort` and `reverse` functions. Finally convert the list of strings to a list of integers with :

```python
intlist = []
for x in slist:
    x = int(x)
    intlist.append(x)
print (intlist)
```

Feel free to experiment with other string, list and dictionary functions. Use the documentation.
