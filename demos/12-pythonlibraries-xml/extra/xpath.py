import sys

from xml.dom import minidom
from xml import xpath

doc = minidom.parse(open(sys.argv[1]))

result =  xpath.Evaluate('/recipe/ingredients/item',doc)
print (result)
