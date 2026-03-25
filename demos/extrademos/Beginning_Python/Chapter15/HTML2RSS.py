#!/usr/bin/env python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor
from xml.parsers.xmlproc import xmlval

class docErrorHandler(xmlval.ErrorHandler):
  def warning(self, message):
    print "Warning: " + message
  def error(self, message):
    print "Error: " + message
  def fatal(self, message):
    print "Fatal: " + message

#Open the stylesheet as a stream
html = open('myblog.html')
xsl = open('HTML2RSS.xsl')

#Parse the streams and build input sources from them
parsedxml = InputSource.DefaultFactory.fromStream(html, "myblog.html")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "HTML2RSS.xsl")

#Create a new processor and attach stylesheet, then transform XML
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

#Write RSS out to a file
output = open("rssfeed.xml", 'w')
output.write(HTML)
output.close

#validate the RSS produced
parser=xmlval.XMLValidator()
parser.set_error_handler(docErrorHandler(parser))
parser.parse_resource("rssfeed.xml")
