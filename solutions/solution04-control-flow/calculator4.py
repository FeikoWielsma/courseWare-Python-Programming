#step 1
resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
while True:
    calc_action = input ("What type of calculation do you want to do :")
    if calc_action == "Quit":
        break
    else:
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calc_action == "Add":
            addresult = f1 + f2
            addlist = [f1, f2, addresult]
            resdict["Add"] = resdict["Add"] + addlist
        elif calc_action == "Subtract":
            subtractresult = f1 - f2
            subtractlist= [f1, f2, subtractresult]
            resdict["Subtract"] = resdict["Subtract"] + subtractlist
        elif calc_action == "Multiply":
            multiplyresult = f1 * f2
            multiplylist = [f1, f2, multiplyresult]
            resdict["Multiply"] = resdict["Multiply"] + multiplylist
        elif calc_action == "Divide":
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
#     calc_action = input("What type of calculation do you want to do :")
#     if calc_action == "Quit":
#         break
#     elif (calc_action == "Sum") or (calc_action == "Average"):
#         s = input("Give a set of numbers separated by space characters : ")
#         slist = s.split(' ')
#         intlist = []
#         sum = 0
#         average = 0
#         if calc_action == "Sum":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             #print("Sum of list %s is %d" %(str(intlist), sum))
#             print(f"Sum of list {intlist} is {sum}")
#         elif calc_action == "Average":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             average = sum / len(intlist)
#             #print("Average of list %s is %f" %(str(intlist), average))
#             print(f"Average of list {intlist} is {average}")
#     elif (calc_action == "Add") or (calc_action == "Subtract") or (calc_action == "Multiply") or (calc_action == "Divide"):
#         f1 = float(input("Give me number 1 : "))
#         f2 = float(input ("Give me number 2 : "))
#         if calc_action == "Add":
#             addresult = f1 + f2
#             addlist = [f1, f2, addresult]
#             resdict["Add"] = resdict["Add"] + addlist
#         elif calc_action == "Subtract":
#             subtractresult = f1 - f2
#             subtractlist= [f1, f2, subtractresult]
#             resdict["Subtract"] = resdict["Subtract"] + subtractlist
#         elif calc_action == "Multiply":
#             multiplyresult = f1 * f2
#             multiplylist = [f1, f2, multiplyresult]
#             resdict["Multiply"] = resdict["Multiply"] + multiplylist
#         elif calc_action == "Divide":
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
# calc_action = "Continue"
# while calc_action != "Quit":
#     calc_action = input("What type of calculation do you want to do :")
#     if (calc_action == "Sum") or (calc_action == "Average"):
#         s = input("Give a set of numbers separated by space characters : ")
#         slist = s.split(' ')
#         intlist = []
#         sum = 0
#         average = 0
#         if calc_action == "Sum":
#             for x in slist:
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             # print("Sum of list %s is %d" %(str(intlist), sum))
#             print(f"Sum of list {intlist} is {sum}")
#
#         elif (calc_action == "Average") :
#             for x in slist :
#                 x = int(x)
#                 sum = sum + x
#                 intlist.append(x)
#             average = sum / len(intlist)
#             #print("Average of list %s is %f" %(str(intlist), average))
#             print(f"Average of list {intlist} is {average}")
#     elif (calc_action == "Add") or (calc_action == "Subtract") or (calc_action == "Multiply") or (calc_action == "Divide"):
#         f1 = float(input("Give me number 1 : "))
#         f2 = float(input ("Give me number 2 : "))
#         if calc_action == "Add":
#             addresult = f1 + f2
#             addlist = [f1, f2, addresult]
#             resdict["Add"] = resdict["Add"] + addlist
#         elif calc_action == "Subtract":
#             subtractresult = f1 - f2
#             subtractlist= [f1, f2, subtractresult]
#             resdict["Subtract"] = resdict["Subtract"] + subtractlist
#         elif calc_action == "Multiply":
#             multiplyresult = f1 * f2
#             multiplylist = [f1, f2, multiplyresult]
#             resdict["Multiply"] = resdict["Multiply"] + multiplylist
#         elif calc_action == "Divide":
#             divideresult = f1 / f2
#             dividelist = [f1, f2, divideresult]
#             resdict["Divide"] = resdict["Divide"] + dividelist
#         # print("Content of dictionary : %s" %(resdict))
#         # print("Length of dictionary : %s" %len(resdict))
#         print(f"Content of dictionary : {resdict}")
#         print(f"Length of dictionary : {len(resdict)}")
#     else:
#         if calc_action != "Quit":
#             print("Incorrect. Available options are 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
# else:
#     print("Thank you for user our software")
