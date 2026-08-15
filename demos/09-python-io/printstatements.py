a = 11
b = 3.5678978
c = True
d = "ABC"

print("Print with str conversions : " + str(a) + " " + str(b) + " " + str(c) + " " + d)

print(f"Print with place holders : {a:10d}  {b:3.2f}  {c!r}  {d} ")

print(f"Print with format function : {a:30}  {b:2.1f}  {c}  {d} ")

print(f"Print with f string : {a:40}  {b:2.4}  {c}  {d} ")  # since Pyton 3.6
