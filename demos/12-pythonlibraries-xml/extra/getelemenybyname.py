from xml.dom import minidom 
xmldoc = minidom.parse('courses.xml') 
title = xmldoc.getElementsByTagName('title')[0].firstChild.data 
print (title)
