import xml.sax


# This handles the parsing of the content
class HandleCollection(xml.sax.ContentHandler):
    def __init__(self):
        print("Inside constructor")

    # Called at the start of an element
    def start_element(self, name, attributes):
        print("Inside startlement : " + name)
        print(attributes)

    # Called at the end of an element
    def end_element(self, name):
        print("Inside endlement : " + name)

    # Called to handle content besides elements
    def characters(self, content):
        print("Inside characters : " + content)


# Parse the collection
parser = xml.sax.make_parser()
parser.set_content_handler(HandleCollection())
parser.parse("courses.xml")
