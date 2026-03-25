#!/usr/bin/python
#
# About the simplest CGI example I could think of.
#
import cgi, cgitb; cgitb.enable()

fields = ["subnum", "reviewer", "comments"]

form = cgi.FieldStorage()
vlist = []
for f in fields:
    vlist.append("%s=%s" % (f, form.getfirst(f)))

print pgtmpl = """Content-Type: text/html

<html><head><title>Hello!</title></head>
%s
</body></html>
""" % "<br>".join(vlist)

