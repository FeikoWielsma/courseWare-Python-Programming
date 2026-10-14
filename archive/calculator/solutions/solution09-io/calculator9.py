from calcu import *

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
calc_action = "Continue"

# The file stays open for the whole session, and `with` closes it on the
# way out however the loop ends.
with open('calculationdata.txt', mode='w', encoding='UTF-8') as fw:
    while calc_action != "Quit":
        calc_action = input("What type of calculation do you want to do :")
        if calc_action == "Faculty":
            try:
                x = int(input("Give a positive integer number : "))
                # print("Faculty of %d is %d" % (x, faculty(x)))
                print(f"Faculty of {x} is {faculty(x)}")
                # fw.write("%s,%s,%s\n" % (calc_action, x, faculty(x)))
                fw.write(f"{calc_action},{x},{faculty(x)}\n")
            except ValueError:
                print("Conversion to positive integer failed. Please try again")
        elif calc_action in {"Sum", "Average"}:
            try:
                s = input("Give a set of numbers separated by space characters : ")
                intlist = convert_to_int_list(s.split(' '))
                if calc_action == "Sum":
                    # print ("Sum of list %s is %d" %(str(intlist), summate(intlist)))
                    # fw.write("%s,%s,%s\n" % (calc_action, str(intlist), summate(intlist)))
                    print(f"Sum of list {intlist} is {summate(intlist)}")
                    fw.write(f"{calc_action},{intlist},{summate(intlist)}\n")
                elif calc_action == "Average":
                    # print ("Average of list %s is %f" %(str(intlist), average(intlist)))
                    # fw.write("%s,%s,%s\n" % (calc_action, str(intlist), average(intlist)))
                    print(f"Average of list {intlist} is {average(intlist)}")
                    fw.write(f"{calc_action},{intlist},{average(intlist)}\n")
            except ValueError:
                print("Not a correct input for an integer list. Please try again")
        elif calc_action in ("Add", "Subtract", "Multiply", "Divide"):
            try:
                f1 = float(input("Give me number 1 : "))
                f2 = float(input ("Give me number 2 : "))
                # fw.write("%s,%s,%s," % (calc_action, str(f1), str(f2)))
                fw.write(f"{calc_action},{f1!s},{f2!s}")
                if calc_action == "Add":
                    addlist = [f1, f2, add (f1, f2)]
                    resdict["Add"] = resdict["Add"] + addlist
                    # fw.write("%s\n" % str(add(f1, f2)))
                    fw.write(f"{add(f1, f2)!s}\n")
                elif calc_action == "Subtract":
                    subtractlist= [f1, f2, subtract (f1, f2)]
                    resdict["Subtract"] = resdict["Subtract"] + subtractlist
                    # fw.write("%s\n" % str(subtract(f1, f2)))
                    fw.write(f"{subtract(f1, f2)!s}\n")
                elif calc_action == "Multiply":
                    multiplylist = [f1, f2, multiply(f1, f2)]
                    resdict["Multiply"] = resdict["Multiply"] + multiplylist
                    # fw.write("%s\n" % str(multiply(f1, f2)))
                    fw.write(f"{multiply(f1, f2)!s}\n")
                elif calc_action == "Divide":
                    try:
                        dividelist = [f1, f2, divide(f1, f2)]
                        resdict["Divide"] = resdict["Divide"] + dividelist
                        # fw.write("%s\n" % str(divide(f1, f2)))
                        fw.write(f"{divide(f1, f2)!s}\n")
                    except ZeroDivisionError:
                        print("Division by zero not allowed. Please try again")
                # print("Content of dictionary : %s" %(resdict))
                # print("Length of dictionary : %s" %len(resdict))
                print(f"Content of dictionary : {resdict}" %())
                print(f"Length of dictionary : {len(resdict)}")
            except ValueError:
                print("Conversion of input to float failed. Please try again")
        else:
            if calc_action!= "Quit":
                print(
                    "Incorrect. Available options are "
                    "'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'"
                )
    print("Thank you for user our software")
