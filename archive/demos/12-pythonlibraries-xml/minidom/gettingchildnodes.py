from xml.dom import minidom

xmldoc = minidom.parse("courses.xml")
print(xmldoc.child_nodes)

print(xmldoc.child_nodes[0])

grammar_node = xmldoc.first_child
print(grammar_node.toxml())


root_node = xmldoc.child_nodes[1]

print(root_node.toxml())
