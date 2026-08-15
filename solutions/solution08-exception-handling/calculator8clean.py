# cleaner code
from calcu import *

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}

def doOneNumberCalculation(calcAction):
    try:
        x = int(input("Give a positive integer number : "))
        # print("Faculty of %d is %d" % (x, faculty(x)))
        print(f"Faculty of {x} is {faculty(x)}")
    except:
        print("Conversion to positive integer failed. Please try again")
        doOneNumberCalculation(calcAction)
def doTwoNumberCalculation(calcAction):
    try:
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calcAction == "Add":
            addlist = [f1, f2, add(f1, f2)]
            resdict["Add"] = resdict["Add"] + addlist
        elif calcAction == "Subtract":
            subtractlist = [f1, f2, subtract(f1, f2)]
            resdict["Subtract"] = resdict["Subtract"] + subtractlist
        elif calcAction == "Multiply":
            multiplylist = [f1, f2, multiply(f1, f2)]
            resdict["Multiply"] = resdict["Multiply"] + multiplylist
        elif calcAction == "Divide":
            try:
                dividelist = [f1, f2, divide(f1, f2)]
                resdict["Divide"] = resdict["Divide"] + dividelist
            except:
                print("Division by zero not allowed. Please try again")
                doTwoNumberCalculation(calcAction)
        # print("Content of dictionary : %s" % (resdict))
        # print("Length of dictionary : %s" % len(resdict))
        print(f"Content of dictionary : {resdict}")
        print(f"Length of dictionary : {len(resdict)}")
    except:
        print("Conversion of input to float failed. Please try again")
        doTwoNumberCalculation(calcAction)

def doListOfNumbersCalculation(calcAction):
    try:
        s = input("Give a set of numbers separated by space characters : ")
        intlist = convertointlist(s.split(' '))
        if calcAction == "Sum":
            # print("Sum of list %s is %d" % (str(intlist), summate(intlist)))
            print(f"Sum of list {intlist} is {summate(intlist)}")
        elif calcAction == "Average":
            # print("Average of list %s is %f" % (str(intlist), average(intlist)))
            print(f"Average of list {intlist} is {average(intlist)}")
    except:
        print("Not a correct input for an integer list. Please try again")
        doListOfNumbersCalculation(calcAction)

def doCalculations():
    calcAction = input("What type of calculation do you want to do :")
    if calcAction == "Faculty":
        doOneNumberCalculation(calcAction)
    elif calcAction in ("Add", "Subtract", "Multiply", "Divide"):
        doTwoNumberCalculation(calcAction)
    elif calcAction == "Sum" or calcAction == "Average":
        doListOfNumbersCalculation(calcAction)
    elif calcAction == "Quit":
        return False
    else:
        print(
            "Incorrect. Available options are "
            "'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'"
        )
    return True

continuecalcu = True
while continuecalcu:
    continuecalcu = doCalculations()
print("Thank you for user our software")

