from employee import Employee, ManagerEmployee, ProgrammerEmployee, WageEmployee


def payroll(staff: list[Employee]) -> float:
    total = 0.0
    for employee in staff:
        salary = employee.calc_salary()  # a different version runs for each type
        print(f"  {employee!s:<28} {salary:>10,.2f}")
        total += salary
    return total


def count_managers(staff: list[Employee]) -> int:
    return sum(1 for employee in staff if isinstance(employee, ManagerEmployee))


class Company:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.staff: list[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.staff.append(employee)

    def fire(self, employee: Employee) -> None:
        self.staff.remove(employee)

    def payroll(self) -> float:
        return payroll(self.staff)

    def breakdown(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for employee in self.staff:
            kind = type(employee).__name__
            totals[kind] = totals.get(kind, 0.0) + employee.calc_salary()
        return totals

    def __str__(self) -> str:
        return f"{self.name} with {len(self.staff)} on the books"


def main() -> None:
    company = Company("SpiralTrain")
    company.hire(WageEmployee("Werner Heisenberg", 2, wage=42.0, hours=160))
    company.hire(ManagerEmployee("Robert Oppenheimer", 3, monthly_salary=8500.0))
    company.hire(ManagerEmployee("Lise Meitner", 4, monthly_salary=9100.0))
    company.hire(ProgrammerEmployee("Grace Hopper", 5, wage=55.0, hours=160, lines=900, bugs=3))

    print(f"{company}\n")
    total = company.payroll()
    print(f"  {'total':<28} {total:>10,.2f}")

    print(f"\nManagers on the payroll: {count_managers(company.staff)}")

    print("\nPer kind of employee:")
    for kind, amount in sorted(company.breakdown().items()):
        print(f"  {kind:<22} {amount:>10,.2f}")

    programmer = company.staff[-1]
    print("\nA programmer is paid by the hour as well:")
    print(f"  isinstance(programmer, WageEmployee)      {isinstance(programmer, WageEmployee)}")
    print(f"  issubclass(ProgrammerEmployee, Employee)  {issubclass(ProgrammerEmployee, Employee)}")


if __name__ == "__main__":
    main()
