# printlinks.py
#
# A Python 2 program that prints links on a web page. 
# Run as a command line tool
#
#    bash % python printlinks.py http://www.python.org
#
# Try running 2to3 on this program and converting it to Python 3.

import urllib
import sys
from HTMLParser import HTMLParser

class LinkPrinter(HTMLParser):
    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for name,value in attrs:
                if name == 'href': print (value)

data = urllib.urlopen(sys.argv[1]).read()
LinkPrinter().feed(data)
