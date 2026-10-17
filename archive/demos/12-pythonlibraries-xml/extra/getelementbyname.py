from xml.dom import minidom

xmldoc = minidom.parse("courses.xml")
title = xmldoc.get_elements_by_tag_name("title")[0].first_child.data
print(title)
