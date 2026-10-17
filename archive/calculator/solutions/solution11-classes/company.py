import employees.employee

e1 = employees.employee.Employee("Albert Einstein")
e2 = employees.employee.Employee("Werner Heisenberg")

employee_list = []

employee_list.append(e1)
employee_list.append(e2)

for e in employee_list:
    # print("Name is : %s and id is : %d" % (e.name, id(e)))
    print(f"Name is : {e.name} and id is : {id(e)}")
