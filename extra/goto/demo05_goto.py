# Example 5: Using a computed goto:
from goto import goto, label

label .getinput
i = raw_input("Enter either 'a', 'b' or 'c', or any other letter to quit: ")
if i in ('a', 'b', 'c'):
    goto *i
else:
    goto .quit

label .a
print "You typed 'a'"
goto .getinput

label .b
print "You typed 'b'"
goto .getinput

label .c
print "You typed 'c'"
goto .getinput

label .quit
print "Finished\n"