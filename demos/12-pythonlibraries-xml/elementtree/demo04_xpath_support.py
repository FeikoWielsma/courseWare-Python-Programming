import xml.etree.ElementTree as ET

# parse XML file and get the courses element
tree = ET.parse("courses.xml")

for elem in tree.iterfind('course/title'):
    print (elem.text)
    
for elem in tree.iterfind('course[@category="JAVA"]/code'):
    print (elem.text)