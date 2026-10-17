import xml.sax

# Create a collection list
collection = []


# This handles the parsing of the content
class HandleCollection(xml.sax.ContentHandler):
    def __init__(self):
        self.course = {}
        self.code = False
        self.title = False
        self.price = False

    # Called at the start of an element
    def start_element(self, name, attributes):
        if name == "code":
            self.code = True
        elif name == "title":
            self.title = True
        elif name == "price":
            self.price = True

    # Called at the end of an element
    def end_element(self, name):
        if name == "course":
            collection.append(self.course)
            self.course = {}
        elif name == "code":
            self.code = False
        elif name == "title":
            self.title = False
        elif name == "price":
            self.price = False

    # Called to handle content besides elements
    def characters(self, content):
        if self.code:
            self.course["code"] = content
        elif self.title:
            self.course["title"] = content
        elif self.price:
            self.course["price"] = content


# Parse the collection
parser = xml.sax.make_parser()
parser.set_content_handler(HandleCollection())
parser.parse("courses.xml")
for course in collection:
    print
    print("Code:  ", course["code"])
    print("Title: ", course["title"])
    print("Price:  ", course["price"])
