str1 = "Hello World!"

print(str1)  # Prints complete string
print(str1[0])  # Prints first character of the string
print(str1[-1])  # Prints last character of the string
print(str1[2:5])  # Prints characters starting from 3rd through 5th
print(str1 * 2)  # Prints string two times
print(str1 + "TEST")  # Prints concatenated string
print(str1[::-1])  # Prints string backwards

var1 = "Hello World!"
var2 = "Python Programming"
print("var1[0]:", var1[0])
print("var2[1:5]:", var2[1:5])

# var1[0] = 'a'  # error

print(id(var1))
var2 = var1[:6] + "Python"
print("Updated String :-", var2)
print(id(var1))
