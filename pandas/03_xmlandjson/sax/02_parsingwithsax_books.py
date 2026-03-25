import xml.sax
# Create a collection list
collection = []
# This handles the parsing of the content
class HandleCollection (xml.sax.ContentHandler):
    def __init__ (self):
        self.course = {}
        self.title = False
        self.author = False
        self.genre = False
    # Called at the start of an element
    def startElement (self, name, attributes):
        if name == 'title':
            self.title = True
        elif name == 'author':
            self.author = True
        elif name == 'genre':
            self.genre = True
    # Called at the end of an element
    def endElement (self, name):
        if name == 'book':
            collection.append (self.book)
            self.book = {}
        elif name == 'title':
            self.title = False
        elif name == 'author':
            self.author = False
        elif name == 'genre':
            self.genre = False
    # Called to handle content besides elements
    def characters (self, content):
        if self.title:
            self.book [ 'title' ] = content
        elif self.author:
            self.book [ 'author' ] = content
        elif self.genre:
            self.book [ 'genre' ] = content

# Parse the collection
parser = xml.sax.make_parser()
parser.setContentHandler (HandleCollection())
parser.parse ('bookcollection.xml')
for book in collection:
    print
    print ('Title:  ', book [ 'title' ])
    print ('Author: ', book [ 'author' ])
    print ('Genre:  ', book [ 'genre' ])