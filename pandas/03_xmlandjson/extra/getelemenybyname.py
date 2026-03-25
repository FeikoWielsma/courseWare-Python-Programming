from xml.dom import minidom 
xmldoc = minidom.parse('courses.03_xmlandjson')
title = xmldoc.getElementsByTagName('title')[0].firstChild.data 
print (title)
