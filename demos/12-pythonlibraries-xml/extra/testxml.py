import xml.etree.ElementTree as xml

root = xml.Element("root")

# Create a child element
child = xml.Element("child")
root.append(child)

# This is how you set an attribute on an element
child.attrib["name"] = "Charlie"

# Now lets write it to an .xml file on the hard drive

# Open a file
file = open("c:/Sun/test.xml", "w")

# Create an ElementTree object from the root element
xml.ElementTree(root).write(file)

# Close the file like a good programmer
file.close()
