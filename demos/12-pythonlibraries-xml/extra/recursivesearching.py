from xml.dom import minidom 
xmldoc = minidom.parse('courses.xml') 
reflist = xmldoc.getElementsByTagName('course')      


firstref = reflist[0]                             
print (firstref.toxml())        

print (reflist[0].toxml())                                
print (reflist[1].toxml()) 
print (reflist[2].toxml())  