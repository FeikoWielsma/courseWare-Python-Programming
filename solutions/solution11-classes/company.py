import employees.employee

e1 = employees.employee.Employee("Albert Einstein")
e2 = employees.employee.Employee("Werner Heisenberg")

employeeList = []

employeeList.append(e1)
employeeList.append(e2)

for e in employeeList:
    # print("Name is : %s and id is : %d" % (e.name, id(e)))
    print(f"Name is : {e.name} and id is : {id(e)}")
