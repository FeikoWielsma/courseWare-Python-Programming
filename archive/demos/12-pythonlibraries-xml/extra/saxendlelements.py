import sys
from xml.sax import saxutils
from xml.sax import make_parser
from xml.sax import handler


class SimpleHandler(saxutils.DefaultHandler):
    def start_element_ns(self, name, qname, attrs):
        print("start_element_ns: ", name, qname)
        for n in attrs.get_names():
            print("  attribute :", n, attrs.get_value(n))

    def end_element_ns(self, name, qname):
        print("end_element_ns: ", name, qname)


parser = make_parser()
sh = SimpleHandler()
parser.set_content_handler(sh)
parser.set_feature(handler.feature_namespaces, 1)
parser.parse(sys.argv[1])
