import os
from xml.etree import ElementTree as ET

try:
    tree = ET.parse("memo.xml")
    print(tree)
    print(tree.write("newmemo.xml"))
except Exception as inst:
    print ("Unexpected error opening %s: %s" % ("memo.xml", inst))
