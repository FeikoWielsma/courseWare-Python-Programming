import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='doc1.xml')
root = tree.getroot()
print (root)

print (root.tag)
print (root.attrib)

for child_of_root in root:
    print (child_of_root.tag, child_of_root.attrib)
    
print (root[0].tag)
print (root[0].text)


for elem in tree.iter():
    print (elem.tag, elem.attrib)
    
for elem in tree.iter(tag='branch'):
    print (elem.tag, elem.attrib)