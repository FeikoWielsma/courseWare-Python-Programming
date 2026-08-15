# step1
# from calcu import *
#
# resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
# calc_action = "Continue"
# while calc_action != "Quit":
#     calc_action = input("What type of calculation do you want to do :")
#     if calc_action == "Faculty":
#         x = int(input("Give a positive integer number : "))
#         fac = calculations.faculty(x)
#         # print("Faculty of %d is %d" %(x , fac))
#         print(f"Faculty of {x} is {fac}")
#     elif (calc_action == "Sum") or (calc_action == "Average"):
#         s = input("Give a set of numbers separated by space characters : ")
#         slist = s.split(' ')
#         intlist = calculations.convert_to_int_list(slist)
#         if calc_action == "Sum":
#             sum = calculations.summate(intlist)
#             # print("Sum of list %s is %d" %(str(intlist), sum))
#             print(f"Sum of list {intlist} is {sum}")
#         elif calc_action == "Average":
#             av = calculations.average(intlist)
#             # print("Average of list %s is %f" %(str(intlist), av))
#             print(f"Average of list {intlist} is {av}")
#     elif (calc_action == "Add") or (calc_action == "Subtract") or (calc_action == "Multiply") or (calc_action == "Divide"):
#         f1 = float(input("Give me number 1 : "))
#         f2 = float(input ("Give me number 2 : "))
#         if calc_action == "Add":
#             addresult = calculations.add(f1, f2)
#             addlist = [f1, f2, addresult]
#             resdict["Add"] = resdict["Add"] + addlist
#         elif (calc_action == "Subtract") :
#             subtractresult = calculations.subtract(f1, f2)
#             subtractlist= [f1, f2, subtractresult]
#             resdict["Subtract"] = resdict["Subtract"] + subtractlist
#         elif calc_action == "Multiply":
#             multiplyresult = calculations.multiply(f1, f2)
#             multiplylist = [f1, f2, multiplyresult]
#             resdict["Multiply"] = resdict["Multiply"] + multiplylist
#         elif calc_action == "Divide":
#             divideresult = calculations.divide(f1, f2)
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
#    print("Thank you for user our software")

#step2
from calcu import *

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
calc_action = "Continue"
while calc_action != "Quit":
    calc_action = input ("What type of calculation do you want to do :")
    if calc_action == "Faculty":
        try:
            x = int(input("Give a positive integer number : "))
            # print("Faculty of %d is %d" %(x , faculty(x)))
            print(f"Faculty of {x} is {faculty(x)}")
        except:
            print("Conversion to positive integer failed. Please try again")
    elif calc_action in {"Sum", "Average"}:
        try:
            s = input("Give a set of numbers separated by space characters : ")
            intlist = convert_to_int_list(s.split(' '))
            if calc_action == "Sum":
                # print("Sum of list %s is %d" %(str(intlist), summate(intlist)))
                print(f"Sum of list {intlist} is {summate(intlist)}")
            elif calc_action == "Average":
                # print("Average of list %s is %f" %(str(intlist), average(intlist)))
                print(f"Average of list {intlist} is {average(intlist)}")
        except:
            print("Not a correct input for an integer list. Please try again")
    elif calc_action in ("Add", "Subtract", "Multiply", "Divide"):
        try:
            f1 = float(input("Give me number 1 : "))
            f2 = float(input ("Give me number 2 : "))
            if calc_action == "Add":
                addlist = [f1, f2, add (f1, f2)]
                resdict["Add"] = resdict["Add"] + addlist
            elif calc_action == "Subtract":
                subtractlist= [f1, f2, subtract(f1, f2)]
                resdict["Subtract"] = resdict["Subtract"] + subtractlist
            elif calc_action == "Multiply":
                multiplylist = [f1, f2, multiply(f1, f2)]
                resdict["Multiply"] = resdict["Multiply"] + multiplylist
            elif calc_action == "Divide":
                try:
                    dividelist = [f1, f2, divide(f1, f2)]
                    resdict["Divide"] = resdict["Divide"] + dividelist
                except:
                    print("Division by zero not allowed. Please try again")
            # print("Content of dictionary : %s" %(resdict))
            # print("Length of dictionary : %s" %len(resdict))
            print(f"Content of dictionary : {resdict}")
            print(f"Length of dictionary : {len(resdict)}")
        except:
            print("Conversion of input to float failed. Please try again")
    else:
        if calc_action != "Quit":
            print(
                "Incorrect. Available options are "
                "'Faculty', 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'"
            )
print("Thank you for user our software")
