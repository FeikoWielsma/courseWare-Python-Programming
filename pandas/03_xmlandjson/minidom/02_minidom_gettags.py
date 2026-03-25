from xml.dom.minidom import parse
dom = parse("courses.xml")
for node in dom.getElementsByTagName('title'):  # visit every node <title /> and its text content
    print (node.toxml())
    print(node.firstChild.data)
