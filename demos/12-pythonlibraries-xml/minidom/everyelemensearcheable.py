from xml.dom import minidom 
xmldoc = minidom.parse('courses.xml') 
reflist = xmldoc.getElementsByTagName('course')      

firstref = reflist[0]                             
print (firstref.toxml()) 

plist = firstref.getElementsByTagName("price")        

print (plist[0].toxml())                            
 
