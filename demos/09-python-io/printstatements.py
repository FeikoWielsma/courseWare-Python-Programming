a = 11
b = 3.5678978
c = True
d = "ABC"

print("Print with str conversions : " + str(a) + " " + str(b) + " " + str(c) + " " + d)

print("Print with place holders : %10d  %3.2f  %r  %s " % (a, b, c, d))

print("Print with format function : {0:30}  {1:2.1f}  {2}  {3} ".format(a, b, c, d))

print(f"Print with f string : {a:40}  {b:2.4}  {c}  {d} ")  # since Pyton 3.6
