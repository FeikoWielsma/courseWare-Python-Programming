from xml.dom.minidom import parse, parseString

dom1 = parse("courses.xml")   # parse an XML file
dom2 = parseString("<course>Some data <empty/> some more data</course>")
print(dom1.toxml())
print(dom2.toxml())