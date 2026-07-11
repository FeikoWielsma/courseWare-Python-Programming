# Exercise 11 : Python Classes

In this exercise you build an Employee class and a Company script around it.

---

### Step 1 : Employee class

Make an `Employee` class representing some employee working in a company in the Python module `employee.py`. The `Employee` class should have two attributes representing the name and the ID of an employee.

Add a constructor to the `Employee` class which sets the attributes when they are passed. Make a simple program which declares an `Employee` object and displays the values of the attributes of the `Employee` object by accessing the attributes directly :

```python
class Employee(object):
    def __init__(self, name):
        print ("Calling Employee constructor")
        self.name = name
```

Next make the attributes private in the `Employee` class and add public set and get member functions to be able to access these attributes. Change the values of the attributes through the accessor functions and display their changed values :

```python
def set_name(self, value):
    self.__name = value

def del_name(self):
    del self.__name
```

Notice that private data cannot be accessed directly from outside of the class. This demonstrates the object oriented principle of encapsulation. In Python there is a workaround so you can still access private data; use this workaround also for demonstration purposes.

Also add a destructor to the class and keep a class variable which counts how many instances of the class are present :

```python
def __del__(self):
    class_name = self.__class__.__name__
    print (class_name, "destroyed")
```

Write print statements when the constructor, destructor, getters and setters are called. Also print an instance variable directly. What is the result?

Next make a property in the class with the following code :

```python
name = property(get_name, set_name, del_name, "name's docstring")
```

Access the `Employee` object through the property as follows :

```python
e1.name = "Some Name"
print (e1.name)
```

Also write statements to show the class and object data :

```python
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
```

Put the `Employee` class in a script in the `employees` package and add code to be able to export the `Employee` class from this package. Give the `Employee` class a `calcSal()` method as follows :

```python
def calcSal(self):
    return 0
```

Optionally you can also add a `hiringdate` attribute to the `Employee` class. Add the following code to test the `Employee` class in stand alone mode :

```python
if __name__ == '__main__':
    main()
```

### Step 2 : Company Script

Make a `Company` script above the `employees` package. Add the necessary import statements to be able to find the `Employee` class in the employee script in the `employees` package. If you keep the `__init__.py` file in the package empty your code could look as follows :

```python
import employees.employee
e1 = employees.employee.Employee("Albert Einstein")
```

Create a number of employees and put them in a list, called for instance `employeeList`. Next iterate through the list and print the name of the employees in the list.

**If time permits** : alternatively you could create a `Company` class with functions to add or to remove employees from the `employeeList`, which displays a list of employees including their name and ID. In that case make a simple script which declares a `Company` object, add several employees to the company and display a list of employees.

The relationship between the `Company` class and the `Employee` class is an association relation of the normal type. We can say every Company employs Employees, or every Employee works for a Company.
