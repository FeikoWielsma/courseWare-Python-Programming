from xml.etree import ElementTree as ET

element = ET.XML("<root><child>One</child><x></x><child>Two</child></root>")

# Create an iterator
for subelement in element:
    print(subelement.text)

print("===")
for subelement in element:
    if subelement.text is not None:
        print(subelement.text)
