from xml.dom.minidom import parse

dom1 = parse("courses.xml")
dom2 = parse("course.xml")
course = dom1.importNode(dom2.childNodes[0], True)  # deep copy
dom1.childNodes[0].appendChild(course)  # append to children of first node in "course.xml"
print (dom1.toxml())
