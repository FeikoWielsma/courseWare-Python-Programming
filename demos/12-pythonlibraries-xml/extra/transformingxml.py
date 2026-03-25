import sys

from xml.dom.ext import PrettyPrint
from xml.dom import minidom

doc = minidom.parse(open(sys.argv[1]))

for n in doc.get_elements_by_tag_name("ingredients"):
    n.tag_name = "ingredientlist"

for n in doc.get_elements_by_tag_name("item"):
    n.tag_name = "ingredient"
    attr = n.get_attribute("num")
    n.set_attribute("quantity", attr)
    n.remove_attribute("num")

PrettyPrint(doc)
