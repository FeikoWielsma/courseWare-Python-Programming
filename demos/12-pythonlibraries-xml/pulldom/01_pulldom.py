from xml.dom.pulldom import START_ELEMENT, parse

doc = parse("courses.xml")
for event, node in doc:
    if event == START_ELEMENT and node.localName == "duration":
        doc.expandNode(node)
        print (node.toxml())