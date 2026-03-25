#step 1
nr1 = 16
nr2 = 23

print(nr1)
print(nr2)

print(type(nr1))
print(type(nr2))

print(id(nr1))
print(id(nr2))

nr1 = 17
nr2 = 24

print(nr1)
print(nr2)

print(id(nr1))
print(id(nr2))

#step 2
addresult = nr1 + nr2
#print ("The result of the addition of : " + str(nr1) + " and " + str(nr2) + " is : ")
#print ("The result of the addition of : %d and %d is : " %(nr1, nr2))
print(f"The result of the addition of : {nr1} and {nr2} is : ")
print(addresult)
print(type(addresult))

# print("The result of the subtraction of : " + str(nr2) + " from " + str(nr1) + " is : ")
print(f"The result of the subtraction of : {nr1} and {nr2} is : ")

subtractresult = nr1 - nr2
print(subtractresult)
print(type(subtractresult))

#print("The result of the multiplication of : " + str(nr1) + " and " + str(nr2) + " is : ")
print(f"The result of the multiplication of : {nr1} and {nr2} is : ")
multiplyresult = nr1 * nr2
print(multiplyresult)
print(type(multiplyresult))

# print("The result of the division of : " + str(nr1) + " by " + str(nr2) + " is : ")
print(f"The result of the division of : {nr1} and {nr2} is : ")
divideresult = nr1 / nr2
print(divideresult)
print(type(divideresult))

#step 3
s1 = input("give me number 1 : ")
s2 = input ("give me number 2 : ")

print(type(s1))
print(type(s2))

#addresult = s1 + s2
addresult = int(s1) + int(s2)

print(addresult)