from xml.etree import ElementTree as ET

element = ET.XML('<root><child val="One"/><child val="Two"/></root>')
for subelement in element:
    print (subelement.attrib)
