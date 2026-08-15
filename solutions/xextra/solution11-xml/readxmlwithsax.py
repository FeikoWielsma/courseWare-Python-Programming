import xml.sax


# This handles the parsing of the content
class HandleCollection (xml.sax.ContentHandler):
    def __init__ (self):
        print ("Inside constructor")
        self.flag = 0
    # Called at the start of an element

    def startElement (self, name, attributes):
        if ((name == "course") and (attributes.get('category') == "JAVA")) :
            print ("Name : " + name)
            self.flag = 1

    # Called at the end of an element
    def endElement (self, name):
        if (name == "course") :
            print ("Inside endlement : " + name)
            self.flag = 0

    # Called to handle content besides elements
    def characters (self, content):
        if (self.flag) :
            print (content)

# Parse the collection
parser = xml.sax.make_parser()
parser.setContentHandler (HandleCollection())
parser.parse ('courses.xml')
