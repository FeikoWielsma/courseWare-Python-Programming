import re

line = "AA-18-XX   WW-11-YY   GG-09-QQ   "
match_list = re.findall(r"[A-Z]{2}-[0-9]{2}-[A-Z]{2}", line, re.M | re.I)
if match_list:
    print("match_list : ", match_list)
else:
    print("No match!!")
