import xml.etree.ElementTree as ET

# parse XML file and get the courses element
tree = ET.parse("courses.xml")
root = tree.getroot()
print(root)  # <Element 'courses' at 0x00F93690>

# What is the root tag
print(root.tag)  # courses

# find element course directly under courses
ele = root.find("course")
print(ele)  # <Element 'course' at 0x01356A80>
print(ele.attrib)  # {'category': 'XML'}

# Create an iterator
for subelement in ele:
    print(subelement.text)  # print text in nodes under course
