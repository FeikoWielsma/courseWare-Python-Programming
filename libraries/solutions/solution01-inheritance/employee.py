from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, employee_id: int) -> None:
        self.name: str = name
        self.employee_id: int = employee_id

    @abstractmethod
    def calc_salary(self) -> float:
        """Every kind of employee has to say how it is paid."""

    def __str__(self) -> str:
        return f"{self.name} (#{self.employee_id})"

    def __repr__(self) -> str:
        # type(self).__name__ rather than a literal, so a subclass says its own name.
        return f"{type(self).__name__}(name={self.name!r}, id={self.employee_id})"


class WageEmployee(Employee):
    def __init__(self, name: str, employee_id: int, wage: float, hours: float) -> None:
        super().__init__(name, employee_id)  # without this line there is no self.name
        self.wage: float = wage
        self.hours: float = hours

    def calc_salary(self) -> float:
        return self.wage * self.hours


class ManagerEmployee(Employee):
    def __init__(self, name: str, employee_id: int, monthly_salary: float) -> None:
        super().__init__(name, employee_id)
        self.monthly_salary: float = monthly_salary

    def calc_salary(self) -> float:
        return self.monthly_salary


class ProgrammerEmployee(WageEmployee):
    LINE_BONUS: float = 1.0
    BUG_PENALTY: float = 20.0

    def __init__(
        self,
        name: str,
        employee_id: int,
        wage: float,
        hours: float,
        lines: int,
        bugs: int,
    ) -> None:
        super().__init__(name, employee_id, wage, hours)
        self.lines: int = lines
        self.bugs: int = bugs

    def calc_salary(self) -> float:
        # Extend the inherited calculation rather than repeating the multiplication.
        base = super().calc_salary()  # wage * hours
        return base + self.lines * self.LINE_BONUS - self.bugs * self.BUG_PENALTY


def main() -> None:
    staff: list[Employee] = [
        WageEmployee("Werner Heisenberg", 2, wage=42.0, hours=160),
        ManagerEmployee("Robert Oppenheimer", 3, monthly_salary=8500.0),
        ProgrammerEmployee("Grace Hopper", 4, wage=55.0, hours=160, lines=900, bugs=3),
    ]

    for employee in staff:
        print(f"{employee!s:<28} {employee.calc_salary():>10,.2f}")

    # print() uses __str__, a list uses __repr__ on each element.
    print(f"\n{staff}")

    print("\nThe abstract base class cannot be built, and neither can an unfinished subclass:")
    try:
        Employee("Nobody In Particular", 99)  # type: ignore[abstract]
    except TypeError as error:
        print(f"  TypeError: {error}")

    class SalesEmployee(Employee):
        """Step 7 : inherits the contract and never honours it."""

    try:
        SalesEmployee("Albert Einstein", 5)
    except TypeError as error:
        print(f"  TypeError: {error}")


if __name__ == "__main__":
    main()
