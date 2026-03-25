import xml.etree.ElementTree as ET

# parse XML file and get the courses element
tree = ET.parse("courses.xml")

for elem in tree.iter():
    print(elem.tag, elem.attrib)

root = tree.getroot()

for course in root.iter("course"):
    print(course.attrib)

courses = root.findall("course")
print(courses)

for course in courses:
    code = course.find("code")
    print(code.text)
