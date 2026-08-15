# Exercise 9 : Python IO

In this exercise every calculation is logged to a text file.

---

### Step 1

Create a project or directory named `exercise9` and a Python module `calculator9.py`. Copy the contents of `calculator8.py` from the previous exercise to `calculator9.py`. Also copy the `calcu` package.

Open a text file for writing just before entering the while loop that asks the user to choose a calculation type. Use a `with` statement, so that the file is closed however the loop ends, and indent the whole loop inside it :

```python
with open('calculationdata.txt', mode='w', encoding='UTF-8') as fw:
    while calc_action != "Quit":
        ...
```

Next add the details of a calculation to a line in this file when each calculation is performed. For the Faculty calculation you could use the following code :

```python
fw.write(f"{calc_action},{x},{faculty(x)}\n")
```

For the Sum and Average calculations you could use the following code :

```python
fw.write(f"{calc_action},{intlist},{summate(intlist)}\n")
```

And for the Add, Subtract, Divide and Multiply calculations you could use the following code just after the input of the numbers :

```python
fw.write(f"{calc_action},{f1},{f2}")
```

And the following code just after each calculation :

```python
fw.write(f"{add(f1, f2)}\n")
```

There is no `fw.close()` to write. Leaving the `with` block closes the file, which is what makes the text appear on disk.

Now enter some calculations to test your code and observe the contents of the file.

### Step 2

Next create a new Python module `readcalculations.py`, read the lines of the file and display its contents with the following code :

```python
with open('calculationdata.txt', encoding='UTF-8') as fr:
    for line in fr:
        s = line.rstrip('\n')
        slist = s.split(',')
        print(slist)
```

Note two things: the file object is iterated directly rather than through `readlines()`, which avoids holding the whole file in memory, and `mode='r'` is left out because reading is the default.

The results could look as follows :

```text
['Faculty', '12', '479001600']
['Sum', '[1', ' 1', ' 3]', '5']
['Average', '[4', ' 5', ' 6]', '5.0']
```
