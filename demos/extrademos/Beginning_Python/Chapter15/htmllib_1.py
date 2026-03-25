#!/usr/bin/env python

# Use this file with the html file "headings.html"

from formatter import AbstractFormatter , DumbWriter
from htmllib import HTMLParser


class HeadingParser(HTMLParser):
  def start_h1(self, tag):
    print "found H1"

writer = DumbWriter()
formatter = AbstractFormatter (writer)
parser=HeadingParser(formatter)
parser.feed(open('headings.html').read())
parser.close()
print "Finished parsing"
