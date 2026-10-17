class Employee:
    """Common base class for all employees."""

    emp_count = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self) -> None:
        print(f"Total Employee {Employee.emp_count}")

    def display_employee(self) -> None:
        print(f"Name : {self.name}, Salary: {self.salary}")


# This would create first object of Employee class
emp1 = Employee("Albert", 2000)
# This would create second object of Employee class
emp2 = Employee("Werner", 5000)

emp1.display_employee()
emp2.display_employee()
print(f"Total Employee {Employee.emp_count}")

emp1.age = 7  # Add an 'age' attribute
emp1.age = 8  # Modify 'age' attribute
del emp1.age  # Delete 'age' attribute

attr = "age"  # an attribute name held in a variable
print(hasattr(emp1, attr))  # True if the attribute exists
setattr(emp1, attr, 8)  # Set or create the attribute
print(getattr(emp1, attr))  # Returns the value of the attribute
delattr(emp1, attr)  # Delete the attribute
print(getattr(emp1, attr, "no age"))  # The default, because the attribute is gone
