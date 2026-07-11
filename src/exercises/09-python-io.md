# Exercise 9 : Python IO

In this exercise every calculation is logged to a text file.

---

### Step 1

Create a project or directory named `exercise9` and a Python module `calculator9.py`. Copy the contents of `calculator8.py` from the previous exercise to `calculator9.py`. Also copy the `calcu` package.

Open a text file for writing just before entering the while loop that asks the user to choose a calculation type :

```python
fw = open('calculationdata.txt', mode='w', encoding='UTF-8')
```

Next add the details of a calculation to a line in this file when each calculation is performed. For the Faculty calculation you could use the following code :

```python
fw.write(f"{calcAction},{x},{faculty(x)}\n")
```

For the Sum and Average calculations you could use the following code :

```python
fw.write(f"{calcAction},{intlist},{summate(intlist)}\n")
```

And for the Add, Subtract, Divide and Multiply calculations you could use the following code just after the input of the numbers :

```python
fw.write(f"{calcAction},{f1},{f2}")
```

And the following code just after each calculation :

```python
fw.write(f"{add(f1, f2)}\n")
```

Finally close the file when you give the `"Quit"` command, otherwise nothing is written :

```python
fw.close()
```

Now enter some calculations to test your code and observe the contents of the file.

### Step 2

Next create a new Python module `readcalculations.py`, read the lines of the file and display its contents with the following code :

```python
fr = open('calculationdata.txt', mode='r', encoding='UTF-8')
for line in fr.readlines():
    s = line.rstrip('\n')
    slist = s.split(',')
    print (slist)
fr.close()
```

The results could look as follows :

```text
['Faculty', '12', '479001600']
['Sum', '[1', ' 1', ' 3]', '5']
['Average', '[4', ' 5', ' 6]', '5.0']
```
