from xml.etree import ElementTree as ET

# create the root </root><root>
root_element = ET.Element("root")

# create the first child <child>One</child>
child = ET.SubElement(root_element, "child")
child.text = "One"

# create the second child <child>Two</child>
child = ET.Element("child")
child.text = "Two"

# now append
root_element.append(child)
# Let's see the results

child = ET.Element("child", val="3")
child.text = "Three"
root_element.append(child)

child = ET.Element("child")
child.text = "Four"
child.set("val", "4")
root_element.append(child)

print(ET.tostring(root_element))
