# A bare except is shown here so the next demo can improve it.
try:
    x = 1
    y = 0
    z = x / y
except:
    print("Cannot divide by zero")

try:
    fh = open("somefile", "r")
except:
    print("Cannot open file")
else:
    fh.close()
