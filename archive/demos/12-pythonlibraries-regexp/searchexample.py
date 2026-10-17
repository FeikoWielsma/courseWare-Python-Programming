import re

line = "Cats are smarter than dogs"
match_obj = re.search(r"(.*) are(\.*)", line, re.M | re.I)
if match_obj:
    print("match_obj.group() : ", match_obj.group())
    print("match_obj.group(1) : ", match_obj.group(1))
    print("match_obj.group(2) : ", match_obj.group(2))
else:
    print("No match!!")
