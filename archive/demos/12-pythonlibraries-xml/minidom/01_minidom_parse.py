from xml.dom.minidom import parse, parse_string

dom1 = parse("courses.xml")  # parse an XML file
dom2 = parse_string("<course>Some data <empty/> some more data</course>")
print(dom1.toxml())
print(dom2.toxml())
