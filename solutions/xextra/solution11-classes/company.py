#import employees.employee
#import employees.wageemployee
#import employees.manageremployee
#import employees.programmeremployee
#
#e1 = employees.employee.Employee("Albert Einstein")
#print (e1.name)
#e1.color = "green"
#print (e1.color)
#e1.color = "red"
#print (e1.color)
#
#w1 = employees.wageemployee.WageEmployee("Werner Heisenberg", 10, 100)
#print (w1.name)
#print (w1.wage)
#print (w1.hours)
##print (w1.color)    # attribute color not defined for WageEmployee
#
#m1 = employees.manageremployee.ManagerEmployee("Robert Oppenheimer", 500)
#print (m1.name)
#print (m1.weeksal)
#
#p1 = employees.programmeremployee.ProgrammerEmployee("Charles Shimenoni", 10, 20, 30, 40)
#print (p1.name)
#print (p1.wage)
#print (p1.hours)
#print (p1.lines)
#print (p1.bugs)
#
#print ("Number of employees : " + str(employees.employee.Employee.empCount))
#
#print ("Beginning iteration")
#
#ar = [e1, w1, m1, p1]
#
#payRoll = 0
#
#for e in ar :
#    print (e.name)
#    print (e.calcSal())
#    payRoll+=e.calcSal()
#
#print ("PayRoll is : ", payRoll)

from employees import *

e1 = Employee("Albert Einstein")
print (e1.name)
e1.color = "green"
print (e1.color)
e1.color = "red"
print (e1.color)

w1 = WageEmployee("Werner Heisenberg", 10, 100)
print (w1.name)
print (w1.wage)
print (w1.hours)
#print w1.color    # attribute color not defined for WageEmployee

m1 = ManagerEmployee("Robert Oppenheimer", 500)
print (m1.name)
print (m1.weeksal)

p1 = ProgrammerEmployee("Charles Shimenoni", 10, 20, 30, 40)
print (p1.name)
print (p1.wage)
print (p1.hours)
print (p1.lines)
print (p1.bugs)

print ("Number of employees : " + str(Employee.empCount))

print ("Beginning iteration")

ar = [e1, w1, m1, p1]

payRoll = 0

for e in ar :
    print (e.name)
    print (e.calcSal())
    payRoll+=e.calcSal()

print ("PayRoll is : ", payRoll)
