from xml.etree import ElementTree as ET

xml_file = "memo.xml"

try:
    tree = ET.parse(xml_file)
except Exception as inst:
    print ("Unexpected error opening %s: %s" % (xml_file, inst))

child = ET.SubElement(tree.getroot(), "child")
child.text = "Three"

try:
    tree.write("newmemo.xml")
except Exception as inst:
    print ("Unexpected error writing to file %s: %s" % (xml_file, inst))


