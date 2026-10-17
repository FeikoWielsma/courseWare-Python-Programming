from xml.etree import ElementTree

# root = ElementTree(file=sys.argv[1])
root = ElementTree.parse("nsexample.xml")

# Create an iterator
iter = root.getiterator()
# Iterate
for element in iter:
    # First the element tag name
    print("Element:", element.tag)
    # Next the attributes (available on the instance itself using
    # the Python dictionary protocol
    if element.keys():
        print("\t_attributes:")
        for name, value in element.items():
            print("\t\t_name: '%s', Value: '%s'" % (name, value))
    # Next the child elements and text
    print("\t_children:")
    # Text that precedes all child elements (may be None)
    if element.text:
        text = element.text
        text = len(text) > 40 and text[:40] + "..." or text
        print("\t\t_text:", repr(text))
    if element.getchildren():
        # Can also use: "for child in element.getchildren():"
        for child in element:
            # Child element tag name
            print("\t\t_element", child.tag)
            # The "tail" on each child element consists of the text
            # that comes after it in the parent element content, but
            # before its next sibling.
            if child.tail:
                text = child.tail
                text = len(text) > 40 and text[:40] + "..." or text
                print("\t\t_text:", repr(text))
