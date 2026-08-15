from employees.employee import Employee


class ManagerEmployee(Employee) :
    def __init__(self, name, weeksal):
        super().__init__(name)
        print ("Calling ManagerEmployee constructor")
        self.__weeksal = weeksal

    def get_weeksal(self):
        print ("inside get_weeksal")
        return self.__weeksal

    def set_weeksal(self, value):
        print ("inside set_weeksal")
        self.__weeksal = value

    def del_weeksal(self):
        print ("inside del_weeksal")
        del self.__weeksal

    weeksal = property(get_weeksal, set_weeksal, del_weeksal, "weeksal's docstring")

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

    def calcSal(self):
        return self.__weeksal

def main():
    m1 = ManagerEmployee("Robert Oppenheimer", 500)
    print (m1.name)
    print (m1.weeksal)
    m1.weeksal = 1000
    print (m1.weeksal)
    print (m1.calcSal())

    print ("ManagerEmployee.__doc__:", ManagerEmployee.__doc__)
    print ("ManagerEmployee.__name__:", ManagerEmployee.__name__)
    print ("ManagerEmployee.__module__:", ManagerEmployee.__module__)
    print ("ManagerEmployee.__bases__:", ManagerEmployee.__bases__)
    print ("ManagerEmployee.__dict__:", ManagerEmployee.__dict__)

if __name__ == '__main__':
    main()
