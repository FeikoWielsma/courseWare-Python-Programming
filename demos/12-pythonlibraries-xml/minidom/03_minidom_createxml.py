from xml.dom.minidom import Document

# Create the minidom document
doc = Document()

# Create the <courses> base element
courses = doc.create_element("courses")
doc.append_child(courses)

# Create the <course> element
course = doc.create_element("course")
course.set_attribute("category", "PROGRAMMING")
courses.append_child(course)

# Create a <code> element
code = doc.create_element("code")
course.append_child(code)

# Give the <code> element some text
codetxt = doc.create_text_node("INT902")
code.append_child(codetxt)

# Create a <title> element
title = doc.create_element("title")
course.append_child(title)

# Give the <title> element some text
titletxt = doc.create_text_node("Python Programming")
title.append_child(titletxt)

price = doc.create_element("price")
course.append_child(price)

# Give the <title> element some text
pricetxt = doc.create_text_node("1000")
price.append_child(pricetxt)

duration = doc.create_element("duration")  # creates <duration />
doc.child_nodes[0].append_child(duration)  # appends at end of 1st child's children


# Print our newly created XML
print(doc.toprettyxml(indent="  "))
# print (doc.toxml())
