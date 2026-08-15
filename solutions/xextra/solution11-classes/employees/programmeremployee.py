from employees.wageemployee import WageEmployee


class ProgrammerEmployee(WageEmployee) :
    def __init__(self, name, wage, hours, lines, bugs):
        super().__init__(name, wage, hours)
        print ("Calling ProgrammerEmployee constructor")
        self.__lines = lines
        self.__bugs = bugs

    def get_lines(self):
        return self.__lines

    def get_bugs(self):
        return self.__bugs

    def set_lines(self, value):
        self.__lines = value

    def set_bugs(self, value):
        self.__bugs = value

    def del_lines(self):
        del self.__lines

    def del_bugs(self):
        del self.__bugs

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

    def calcSal(self):
        return self.get_wage()*self.get_hours()+self.__lines - self.__bugs

    lines = property(get_lines, set_lines, del_lines, "lines's docstring")
    bugs = property(get_bugs, set_bugs, del_bugs, "bugs's docstring")

def main():
    p1 = ProgrammerEmployee("Charles Shimenoni", 10, 20, 50, 60)
    print (p1.name)
    print (p1.wage)
    print (p1.hours)
    print (p1.lines)
    print (p1.bugs)
    print ("Salary : ",  p1.calcSal())
#    p1.bugs=11111
#    print p1.bugs

    print ("ProgrammerEmployee.__doc__:", ProgrammerEmployee.__doc__)
    print ("ProgrammerEmployee.__name__:", ProgrammerEmployee.__name__)
    print ("ProgrammerEmployee.__module__:", ProgrammerEmployee.__module__)
    print ("ProgrammerEmployee.__bases__:", ProgrammerEmployee.__bases__)
    print ("ProgrammerEmployee.__dict__:", ProgrammerEmployee.__dict__)

if __name__ == '__main__':
    main()
