import re
line = "AA-18-XX   WW-11-YY   GG-09-QQ   ";
matchObj = re.match( r'[A-Z]{2}-[0-9]{2}-[A-Z]{2}', line, re.M|re.I)
if matchObj:
    print ("matchObj.group() : ", matchObj.group())
else:
    print ("No match!!")
