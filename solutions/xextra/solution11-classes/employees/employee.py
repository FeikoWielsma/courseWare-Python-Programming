class Employee:
    empCount = 0
    def __init__(self, name):
        print ("Calling Employee constructor")
        self.__name = name
        Employee.empCount+=1

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def del_name(self):
        del self.__name

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    name = property(get_name, set_name, del_name, "name's docstring")

    def calcSal(self):
        return 0

def main():
    e1 = Employee("Albert Einstein")
    print (e1._Employee__name)
    e1.name = "Pipo de Clown"
    print (e1.name)
    print (e1)
    print ("Salary is : ", e1.calcSal())

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


#   def __init__(self, name, salary):
#
#      self.salary = salary
#      Employee.empCount += 1
#   def displayCount(self):
#     print "Total Employee %d" % Employee.empCount
#   def displayEmployee(self):
#      print "Name : ", self.name,  ", Salary: ", self.salary


#    public String getName() {
#        return name;
#    }
#
#    public void setName(String s) {
#        s = name;
#    }
#}
# Java Code
#package employees;
#
#public class Employee {
#    private String name;
#
#    public Employee() {
#        name = "Empty";
#    }
#
#    public Employee(String s) {
#        name = s;
#    }
#
#    public String getName() {
#        return name;
#    }
#
#    public void setName(String s) {
#        s = name;
#    }
#}
