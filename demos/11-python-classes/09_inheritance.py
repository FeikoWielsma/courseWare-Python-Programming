class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team: list[str]) -> None:
        super().__init__(name, salary)  # the Employee part
        self.team = team  # what a Manager adds

    def describe(self) -> str:  # replaces Employee.describe
        return f"{super().describe()} and leads {len(self.team)} people"


emp = Employee("Werner", 5000)
boss = Manager("Marie", 6000, ["Albert", "Werner"])
print(emp.describe())
print(boss.describe())
print(boss.name)  # inherited from Employee.__init__
print(isinstance(boss, Employee))
