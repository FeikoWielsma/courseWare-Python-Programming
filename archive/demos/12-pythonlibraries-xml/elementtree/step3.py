import xml.etree.ElementTree as ET

tree = ET.ElementTree(file="doc1.xml")

root = tree.getroot()
del root[2]

root[0].set("foo", "bar")

for subelem in root:
    print(subelem.tag, subelem.attrib)

tree.write("new1.xml")

a = ET.Element("elem")
c = ET.SubElement(a, "child1")
c.text = "some text"
d = ET.SubElement(a, "child2")
b = ET.Element("elem_b")
root = ET.Element("root")
root.extend((a, b))
tree = ET.ElementTree(root)

tree.write("new2.xml")
