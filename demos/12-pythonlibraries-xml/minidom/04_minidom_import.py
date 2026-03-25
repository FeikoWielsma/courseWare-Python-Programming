from xml.dom.minidom import parse

dom1 = parse("courses.xml")
dom2 = parse("course.xml")
course = dom1.import_node(dom2.child_nodes[0], True)  # deep copy
dom1.child_nodes[0].append_child(
    course
)  # append to children of first node in "course.xml"
print(dom1.toxml())
