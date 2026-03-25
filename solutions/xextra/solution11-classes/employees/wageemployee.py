from employees.employee import Employee

class WageEmployee(Employee) :   
    def __init__(self, name, wage, hours):
        super(WageEmployee,self).__init__(name)  
        print ("Calling WageEmployee constructor")
        self.__wage = wage
        self.__hours = hours

    def get_wage(self):
        return self.__wage

    def get_hours(self):
        return self.__hours

    def set_wage(self, value):
        self.__wage = value

    def set_hours(self, value):
        self.__hours = value

    def del_wage(self):
        del self.__wage

    def del_hours(self):
        del self.__hours

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
        
    def calcSal(self):
        return self.__wage * self.__hours    
    
    wage = property(get_wage, set_wage, del_wage, "wage's docstring")
    hours = property(get_hours, set_hours, del_hours, "hours's docstring")
          
def main():
    w1 = WageEmployee("Werner Heisenberg", 10, 33)
    print (w1.name)
    print (w1.wage)
    print (w1.hours)
    
    print ("Salary : ",  w1.calcSal())
    
    print ("WageEmployee.__doc__:", WageEmployee.__doc__)
    print ("WageEmployee.__name__:", WageEmployee.__name__)
    print ("WageEmployee.__module__:", WageEmployee.__module__)
    print ("WageEmployee.__bases__:", WageEmployee.__bases__)
    print ("WageEmployee.__dict__:", WageEmployee.__dict__)

if __name__ == '__main__':
    main()
