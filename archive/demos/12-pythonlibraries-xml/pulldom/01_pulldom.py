from xml.dom.pulldom import START_ELEMENT, parse

doc = parse("courses.xml")
for event, node in doc:
    if event == START_ELEMENT and node.local_name == "duration":
        doc.expand_node(node)
        print(node.toxml())
