from xml.dom.minidom import Document

# Create the minidom document
doc = Document()

# Create the <courses> base element
courses = doc.createElement("courses")
doc.appendChild(courses)

# Create the <course> element
course = doc.createElement("course")
course.setAttribute("category", "PROGRAMMING")
courses.appendChild(course)

# Create a <code> element
code = doc.createElement("code")
course.appendChild(code)

# Give the <code> element some text
codetxt = doc.createTextNode("INT902")
code.appendChild(codetxt)

# Create a <title> element
title = doc.createElement("title")
course.appendChild(title)

# Give the <title> element some text
titletxt = doc.createTextNode("Python Programming")
title.appendChild(titletxt)

price = doc.createElement("price")
course.appendChild(price)

# Give the <title> element some text
pricetxt = doc.createTextNode("1000")
price.appendChild(pricetxt)

duration = doc.createElement("duration")  # creates <duration />
doc.childNodes[0].appendChild(duration)  # appends at end of 1st child's children


# Print our newly created XML
print (doc.toprettyxml(indent="  "))
#print (doc.toxml())
