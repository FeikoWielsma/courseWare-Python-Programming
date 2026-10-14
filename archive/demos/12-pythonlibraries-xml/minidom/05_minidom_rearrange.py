import pprint

import xml.dom.minidom
from xml.dom.minidom import Node

doc = xml.dom.minidom.parse("books.xml")

mapping = {}

for node in doc.get_elements_by_tag_name("book"):
    isbn = node.get_attribute("isbn")
    titles = node.get_elements_by_tag_name("title")
    for node2 in titles:
        title = ""
        for node3 in node2.child_nodes:
            if node3.node_type == Node.TEXT_NODE:
                title += node3.data
    mapping[isbn] = title

# mapping now has the same value as in the SAX example:
pprint.pprint(mapping)
