class Employee :
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
print Employee.empCount
emp2 = Employee("Zara", 2000)
print Employee.empCount
emp3 = Employee("Zara", 2000)
#print Employee.name