import re

line = "AA-18-XX   WW-11-YY   GG-09-QQ   ";

matchList = re.findall( r'[A-Z]{2}-[0-9]{2}-[A-Z]{2}', line, re.M|re.I)
if matchList:
    print ("matchList : ", matchList)
else:
    print ("No match!!")
