from xml.dom import minidom                                         
xmldoc = minidom.parse('courses.xml') 
print (xmldoc.childNodes)                                  

print (xmldoc.childNodes[0])                               

grammarNode = xmldoc.firstChild 
print (grammarNode.toxml())


rootNode = xmldoc.childNodes[1] 

print (rootNode.toxml())