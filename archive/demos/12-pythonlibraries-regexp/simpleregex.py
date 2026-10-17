import re

line = "AA-18-XX   WW-11-YY   GG-09-QQ   "
match_obj = re.match(r"[A-Z]{2}-[0-9]{2}-[A-Z]{2}", line, re.M | re.I)
if match_obj:
    print("match_obj.group() : ", match_obj.group())
else:
    print("No match!!")
