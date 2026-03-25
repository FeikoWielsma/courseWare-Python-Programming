from xml.dom import minidom

xmldoc = minidom.parse('courses.xml')
print (xmldoc.childNodes)                                  

print (xmldoc.childNodes[0])                               

rootNode = xmldoc.firstChild
print (rootNode.toxml())

