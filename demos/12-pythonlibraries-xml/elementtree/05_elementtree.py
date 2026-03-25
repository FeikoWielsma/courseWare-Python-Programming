import os
from xml.etree import ElementTree as ET

xml_file = os.path.abspath(__file__)
xml_file = os.path.dirname(xml_file)
xml_file = os.path.join(xml_file, "memo.xml")

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
    return

