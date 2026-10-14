from xml.dom import minidom

xmldoc = minidom.parse("courses.xml")
reflist = xmldoc.get_elements_by_tag_name("course")

firstref = reflist[0]
print(firstref.toxml())

plist = firstref.get_elements_by_tag_name("price")

print(plist[0].toxml())
