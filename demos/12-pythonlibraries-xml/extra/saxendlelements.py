import sys
from xml.sax import saxutils
from xml.sax import make_parser
from xml.sax import handler

class SimpleHandler(saxutils.DefaultHandler):
    def startElementNS(self,name,qname,attrs):
        print ('startElementNS: ', name,qname)
        for n in attrs.getNames():
            print ("  attribute :", n, attrs.getValue(n))
          
    def endElementNS(self,name,qname):
        print ('endElementNS: ', name, qname)

parser = make_parser()
sh = SimpleHandler()
parser.setContentHandler(sh)
parser.setFeature(handler.feature_namespaces,1)
parser.parse(sys.argv[1])
