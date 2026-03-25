import xml.sax

# Create a collection list
collection = []


# This handles the parsing of the content
class HandleCollection(xml.sax.ContentHandler):
    def __init__(self):
        self.data = {}
        self.master_tu = False

    # Called at the start of an element
    def start_element(self, name, attributes):
        if name == "es:master_tu":
            print("found start")
            self.master_tu = True

    # Called at the end of an element
    def end_element(self, name):
        #        if name == 'xn:VsDataContainer':
        #            print ("found container")
        #            collection.append (self.data)
        #            self.data = {}
        if name == "es:master_tu":
            print("found end")
            self.master_tu = False
            collection.append(self.data)
            self.data = {}

    # Called to handle content besides elements
    def characters(self, content):
        if self.master_tu:
            self.data["master_tu"] = content


# Parse the collection
parser = xml.sax.make_parser()
parser.set_content_handler(HandleCollection())
parser.parse("Topology_ttrc_20110118.xml")
for data in collection:
    print
    print("Data:  ", data["master_tu"])
