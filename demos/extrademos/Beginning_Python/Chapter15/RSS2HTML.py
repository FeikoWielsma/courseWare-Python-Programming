#!/usr/bin/python

from Ft.Xml import InputSource
from Ft.Xml.Xslt.Processor import Processor

#Open the stylesheet as a stream
xsl = open('RSS2HTML.xsl')

#Parse the streams and build input sources from them
parsedxml = InputSource.DefaultFactory.fromUri("http://www.newscientist.com/feed.ns?index=mars-rovers&type=xml ")
parsedxsl = InputSource.DefaultFactory.fromStream(xsl, "RSS2HTML.xsl")

#Create a new processor and attach stylesheet, then transform XML
processor = Processor()
processor.appendStylesheet(parsedxsl)
HTML = processor.run(parsedxml)

#Write HTML out to a file
output = open("aggregator.html", 'w')
output.write(HTML)
output.close
