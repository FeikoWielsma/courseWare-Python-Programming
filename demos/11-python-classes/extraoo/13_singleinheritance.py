class Employee:  # define parent class
    def __init__(self, name):
        print("Inside Employee constructor")
        self.name = name

    def calc_salary(self):
        print("Inside calc_salary of Employee")
        self.salary = 0
        return self.salary

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class WageEmployee(Employee):  # define child class
    def __init__(self, name, wage, hours):
        print("Inside WageEmployee constructor")
        super().__init__(name)
        # Employee.__init__(self, name)     # alternative
        self.wage = wage
        self.hours = hours

    def set_wage(self, wage):
        self.wage = wage

    def get_wage(self):
        return self.wage

    def set_hours(self, hours):
        self.hours = hours

    def get_hours(self):
        return self.hours


e = Employee("Employee 1")
w = WageEmployee("WageEmployee 1", 10, 10)

print(e.get_name())
print(e.calc_salary())

print(w.get_name())
print(w.calc_salary())
print(w.get_wage())
print(w.get_hours())
