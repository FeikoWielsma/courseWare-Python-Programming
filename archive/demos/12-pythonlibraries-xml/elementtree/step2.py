import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="doc1.xml")

for elem in tree.iterfind("branch/sub-branch"):
    print(elem.tag, elem.attrib)

for elem in tree.iterfind('branch[@name="release01"]'):
    print(elem.tag, elem.attrib)
