# Exercise 7 : Comprehensions

In this exercise functions are replaced by functional programming constructs like lambdas, comprehensions and `reduce`.

---

### Step 1

Create a project or directory named `exercise7` and a Python module `calculator7.py`. Copy the contents of `calculator6.py` from the previous exercise to `calculator7.py`. Do not copy the `calcu` package.

Put the import `from functools import reduce` in the first line of `calculator7.py`.

### Step 2

Replace the following code by a list comprehension :

```python
s = input("Give a set of numbers separated by space characters : ")
slist = s.split(' ')
intlist = convertointlist(slist)
```

We do not need a `convertointlist` function because we can do the conversion in a one-liner using a list comprehension.

### Step 3

Replace the following code by a call to the `reduce` function which uses a lambda function for summing :

```python
summation = summate(intlist)
print (f"Sum of list {intlist} is {summation}")
```

### Step 4

Replace the following code by a call to the `reduce` function which uses a lambda function for summing, and divide by the length of the list of integers :

```python
av = average(intlist)
print (f"Average of list {intlist} is {av}")
```

We can calculate the average in a one-liner using the `reduce` function, a lambda and the length of the list with the `len` function.

### Step 5

Replace the following code with one line which uses the definition and call of a lambda function for `add`. Do the same for `subtract`, `divide` and `multiply`. All can be replaced by one-liners which do not use an external function :

```python
addresult = add(f1, f2)
addlist = [f1, f2, addresult]
resdict["Add"] = resdict["Add"] + addlist
```

### Step 6

Finally replace the calculation of the factorial with the following code and observe that it gives the correct results :

```python
n = int(input("Give a positive integer number : "))
fac = reduce((lambda x, y: x * y), list(range(1, n+1)))
```
