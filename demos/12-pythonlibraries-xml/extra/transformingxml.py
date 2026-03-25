import sys

from xml.dom.ext import PrettyPrint
from xml.dom import minidom

doc = minidom.parse(open(sys.argv[1]))

for n in doc.getElementsByTagName("ingredients"):
    n.tagName = "ingredientlist"

for n in doc.getElementsByTagName("item"):
    n.tagName = "ingredient"
    attr = n.getAttribute("num")
    n.setAttribute("quantity",attr)
    n.removeAttribute("num")

PrettyPrint(doc)