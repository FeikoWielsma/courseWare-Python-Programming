class Employee:
    emp_count = 0
    def __init__(self, name: str) -> None:
        print ("Calling Employee constructor")
        self.__name = name
        Employee.emp_count += 1

    def get_name(self) -> str:
        return self.__name

    def set_name(self, value: str) -> None:
        self.__name = value

    def del_name(self) -> None:
        del self.__name

    def __del__(self) -> None:
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    name = property(get_name, set_name, del_name, "name's docstring")

    def calc_salary(self) -> float:
        return 0

def main() -> None:
    e1 = Employee("Albert Einstein")
    print (e1._Employee__name)
    e1.name = "Pipo de Clown"
    print(e1.name)
    print(e1)
    print("Salary is : ", e1.calc_salary())

    e2 = Employee("Werner von Braun")
    print (e2._Employee__name)
    e2.name = "Mamaloe"
    print (e2.name)
    print (e2)

    print ("Employee.__doc__:", Employee.__doc__)
    print ("Employee.__name__:", Employee.__name__)
    print ("Employee.__module__:", Employee.__module__)
    print ("Employee.__bases__:", Employee.__bases__)
    print ("Employee.__dict__:", Employee.__dict__)

if __name__ == '__main__':
    main()
