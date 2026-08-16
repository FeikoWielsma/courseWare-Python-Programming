"""Solution to Exercise 12, step 6 : the Employee class, annotated."""


class Employee:
    """An employee with a name and a salary."""

    emp_count: int = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self) -> None:
        """Print how many employees have been created."""
        print(f"Total Employee {Employee.emp_count}")

    def display_employee(self) -> None:
        """Print this employee's details."""
        print(f"Name : {self.name}, Salary: {self.salary}")

    def calc_salary(self) -> float:
        """Return the salary. `self` is never annotated."""
        return self.salary


emp1 = Employee("Albert", 2000)
emp2 = Employee("Werner", 5000)
emp1.display_employee()
emp2.display_employee()
emp1.display_count()
