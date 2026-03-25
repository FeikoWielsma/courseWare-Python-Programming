import cgi
import sys

form = cgi.FieldStorage()
for name in form.keys():
    print >> sys.stderr, name, "=>", form[name].value
