import xml.sax
# Create a collection list
collection = []
# This handles the parsing of the content
class HandleCollection (xml.sax.ContentHandler):
    def __init__ (self):
        self.data = {}
        self.masterTU = False
    # Called at the start of an element
    def startElement (self, name, attributes):
        if name == 'es:masterTu':
            print ("found start")
            self.masterTU = True
    # Called at the end of an element
    def endElement (self, name):
#        if name == 'xn:VsDataContainer':
#            print ("found container")
#            collection.append (self.data)
#            self.data = {}
        if name == 'es:masterTu':
            print ("found end")
            self.masterTU = False
            collection.append (self.data)
            self.data = {}

    # Called to handle content besides elements
    def characters (self, content):
        if self.masterTU:
            self.data [ 'masterTu' ] = content

# Parse the collection
parser = xml.sax.make_parser()
parser.setContentHandler (HandleCollection())
parser.parse ('Topology_ttrc_20110118.xml')
for data in collection:
    print
    print ('Data:  ', data [ 'masterTu' ])