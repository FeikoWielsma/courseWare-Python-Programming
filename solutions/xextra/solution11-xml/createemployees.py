from xml.dom.minidom import Document

# Create the minidom document
doc = Document()

# Create the <employees> base element
employees = doc.createElement("employees")
doc.appendChild(employees)

# Create the <employee> element
employee = doc.createElement("employee")
employees.appendChild(employee)
employee.setAttribute("type", "emp")

# Create a <name> element
name = doc.createElement("name")
employee.appendChild(name)

# Give the <name> element some text
nametxt = doc.createTextNode("Albert Einstein")
name.appendChild(nametxt)

# Create a <id> element
id = doc.createElement("id")
employee.appendChild(id)

# Give the <id> element some text
idtxt = doc.createTextNode("11111")
id.appendChild(idtxt)

# Create a <ssn> element
ssn = doc.createElement("ssn")
employee.appendChild(ssn)

# Give the <ssn> element some text
ssntxt = doc.createTextNode("123456789")
ssn.appendChild(ssntxt)

# Create a <age> element
age = doc.createElement("age")
employee.appendChild(age)

# Give the <age> element some text
agetxt = doc.createTextNode("55")
age.appendChild(agetxt)

# Create a <hiringDate> element
hiringDate = doc.createElement("hiringDate")
employee.appendChild(hiringDate)

# Give the <age> element some text
hiringDatetxt = doc.createTextNode("11-12-1953")
hiringDate.appendChild(hiringDatetxt)


#Add another employee with the type attribute wageemployee and xextra fields for wage and hours :
# Create the <employee> element
employee = doc.createElement("employee")
employees.appendChild(employee)
employee.setAttribute("type", "wageemp")

# etc

# Create a <wage> element
wage = doc.createElement("wage")
employee.appendChild(wage)

# Give the <wage> element some text
wagetxt = doc.createTextNode("10")
wage.appendChild(wagetxt)

# Create a <hours> element
hours = doc.createElement("hours")
employee.appendChild(hours)

# Give the <hours> element some text
hourstxt = doc.createTextNode("10")
hours.appendChild(hourstxt)

#Add another employee with type attribute manageremployee and an xextra field for weeksal :

employee = doc.createElement("employee")
employees.appendChild(employee)
employee.setAttribute("type", "manageremp")

# etc

# Create a <weeksal> element
weeksal = doc.createElement("weeksal")
employee.appendChild(weeksal)

# Give the <weeksal> element some text
weeksaltxt = doc.createTextNode("10")
weeksal.appendChild(weeksaltxt)

#And finally add another employee with type attribute programmeremployee and an xextra fields for wage, hours, lines and bugs :

employee = doc.createElement("employee")
employees.appendChild(employee)
employee.setAttribute("type", "programmeremp")

# etc

# Create a <lines> element
lines = doc.createElement("lines")
employee.appendChild(lines)

# Give the <lines> element some text
linestxt = doc.createTextNode("10")
lines.appendChild(linestxt)

# Create a <bugs> element
bugs = doc.createElement("bugs")
employee.appendChild(bugs)

# Give the <busg> element some text
bugstxt = doc.createTextNode("10")
bugs.appendChild(bugstxt)


#Write the xml to the console with :

# Print our newly created XML
print (doc.toprettyxml(indent="  "))
