from xml.dom.minidom import parse

dom = parse("courses.xml")
for node in dom.get_elements_by_tag_name("title"):  # visit every node <title />
    # print (dom.node_name)
    print(node.toxml())
