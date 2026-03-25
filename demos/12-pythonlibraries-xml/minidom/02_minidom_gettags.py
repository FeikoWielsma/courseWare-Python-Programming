from xml.dom.minidom import parse
dom = parse("courses.xml")
for node in dom.getElementsByTagName('title'):  # visit every node <title />
    #print (dom.nodeName)
    print (node.toxml())
