#step 1
resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
while True:
    calcAction = input ("What type of calculation do you want to do :")
    if calcAction == "Quit":
        break
    else:
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calcAction == "Add":
            addresult = f1 + f2
            addlist = [f1, f2, addresult]
            resdict["Add"] = resdict["Add"] + addlist
        elif calcAction == "Subtract":
            subtractresult = f1 - f2
            subtractlist= [f1, f2, subtractresult]
            resdict["Subtract"] = resdict["Subtract"] + subtractlist
        elif calcAction == "Multiply":
            multiplyresult = f1 * f2
            multiplylist = [f1, f2, multiplyresult]
            resdict["Multiply"] = resdict["Multiply"] + multiplylist
        elif calcAction == "Divide":
            divideresult = f1 / f2
            dividelist = [f1, f2, divideresult]
            resdict["Divide"] = resdict["Divide"] + dividelist
        else:
            print("Incorrect. Available options are 'Add', 'Subtract, 'Multiply, 'Divide'")
        # print("Content of dictionary : %s" %(resdict))
        # print("Length of dictionary : %s" %len(resdict))
        print(f"Content of dictionary : {resdict}")
        print(f"Length of dictionary : {len(resdict)}")
print("Thank you for user out software")
#step 2
# resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
# while True:
#     calcAction = input("What type of calculation do you want to do :")
#     if calcAction == "Quit":
#         break
#     elif (calcAction == "Sum") or (calcAction == "Average"):
#         s = input("Give a set of numbers separated by space characters : ")
#         slist = s.split(' ')
#         intlist = []
#         sum = 0
#         average = 0
#         if calcAction == "Sum":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             #print("Sum of list %s is %d" %(str(intlist), sum))
#             print(f"Sum of list {intlist} is {sum}")
#         elif calcAction == "Average":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             average = sum / len(intlist)
#             #print("Average of list %s is %f" %(str(intlist), average))
#             print(f"Average of list {intlist} is {average}")
#     elif (calcAction == "Add") or (calcAction == "Subtract") or (calcAction == "Multiply") or (calcAction == "Divide"):
#         f1 = float(input("Give me number 1 : "))
#         f2 = float(input ("Give me number 2 : "))
#         if calcAction == "Add":
#             addresult = f1 + f2
#             addlist = [f1, f2, addresult]
#             resdict["Add"] = resdict["Add"] + addlist
#         elif calcAction == "Subtract":
#             subtractresult = f1 - f2
#             subtractlist= [f1, f2, subtractresult]
#             resdict["Subtract"] = resdict["Subtract"] + subtractlist
#         elif calcAction == "Multiply":
#             multiplyresult = f1 * f2
#             multiplylist = [f1, f2, multiplyresult]
#             resdict["Multiply"] = resdict["Multiply"] + multiplylist
#         elif calcAction == "Divide":
#             divideresult = f1 / f2
#             dividelist = [f1, f2, divideresult]
#             resdict["Divide"] = resdict["Divide"] + dividelist
#         # print("Content of dictionary : %s" %(resdict))
#         # print("Length of dictionary : %s" %len(resdict))
#         print(f"Content of dictionary : {resdict}")
#         print(f"Length of dictionary : {len(resdict)}")
#     else:
#         print("Incorrect. Available options are 'Sum, 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
# print("Thank you for user our software")

#step 3
# resdict = {"Add": [], "Subtract": [], "Multiply": [],"Divide": []}
# calcAction = "Continue"
# while calcAction != "Quit":
#     calcAction = input("What type of calculation do you want to do :")
#     if (calcAction == "Sum") or (calcAction == "Average"):
#         s = input("Give a set of numbers separated by space characters : ")
#         slist = s.split(' ')
#         intlist = []
#         sum = 0
#         average = 0
#         if calcAction == "Sum":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             # print("Sum of list %s is %d" %(str(intlist), sum))
#             print(f"Sum of list {intlist} is {sum}")
#
#         elif (calcAction == "Average") :
#             for x in slist :
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             average = sum / len(intlist)
#             #print("Average of list %s is %f" %(str(intlist), average))
#             print(f"Average of list {intlist} is {average}")
#     elif (calcAction == "Add") or (calcAction == "Subtract") or (calcAction == "Multiply") or (calcAction == "Divide"):
#         f1 = float(input("Give me number 1 : "))
#         f2 = float(input ("Give me number 2 : "))
#         if calcAction == "Add":
#             addresult = f1 + f2
#             addlist = [f1, f2, addresult]
#             resdict["Add"] = resdict["Add"] + addlist
#         elif calcAction == "Subtract":
#             subtractresult = f1 - f2
#             subtractlist= [f1, f2, subtractresult]
#             resdict["Subtract"] = resdict["Subtract"] + subtractlist
#         elif calcAction == "Multiply":
#             multiplyresult = f1 * f2
#             multiplylist = [f1, f2, multiplyresult]
#             resdict["Multiply"] = resdict["Multiply"] + multiplylist
#         elif calcAction == "Divide":
#             divideresult = f1 / f2
#             dividelist = [f1, f2, divideresult]
#             resdict["Divide"] = resdict["Divide"] + dividelist
#         # print("Content of dictionary : %s" %(resdict))
#         # print("Length of dictionary : %s" %len(resdict))
#         print(f"Content of dictionary : {resdict}")
#         print(f"Length of dictionary : {len(resdict)}")
#     else:
#         if calcAction != "Quit":
#             print("Incorrect. Available options are 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
# else:
#     print("Thank you for user our software")
