import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='courses.xml')

count = 0
for elem in tree.iter(tag='vendor'):
    if elem.text == 'Twice':
        count += 1

print (count)

count = 0
for event, elem in ET.iterparse('courses.xml'):
    if event == 'end':
        if elem.tag == 'vendor' and elem.text == 'Twice':
            count += 1
    elem.clear() # discard the element

print (count)