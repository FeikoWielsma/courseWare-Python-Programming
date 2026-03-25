#!/usr/bin/python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor

#Open the XML and stylesheet as streams
xml = open('library.xml')
xsl = open('HTMLLibrary.xsl')

#Parse the streams and build input sources from them
parsedxml = InputSource.DefaultFactory.fromStream(xml , "library.xml")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "HTMLLibrary.xsl")

#Create a new processor and attach stylesheet, then transform XML
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

#Write HTML out to a file
output = open("library.html", 'w')
output.write(HTML)
output.close
