# cleaner code
from calcu import *

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}

def do_one_number_calculation(calc_action: str) -> None:
    try:
        x = int(input("Give a positive integer number : "))
        # print("Faculty of %d is %d" % (x, faculty(x)))
        print(f"Faculty of {x} is {faculty(x)}")
    except:
        print("Conversion to positive integer failed. Please try again")
        do_one_number_calculation(calc_action)
def do_two_number_calculation(calc_action: str) -> None:
    try:
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calc_action == "Add":
            addlist = [f1, f2, add(f1, f2)]
            resdict["Add"] = resdict["Add"] + addlist
        elif calc_action == "Subtract":
            subtractlist = [f1, f2, subtract(f1, f2)]
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
                do_two_number_calculation(calc_action)
        # print("Content of dictionary : %s" % (resdict))
        # print("Length of dictionary : %s" % len(resdict))
        print(f"Content of dictionary : {resdict}")
        print(f"Length of dictionary : {len(resdict)}")
    except:
        print("Conversion of input to float failed. Please try again")
        do_two_number_calculation(calc_action)

def do_list_of_numbers_calculation(calc_action: str) -> None:
    try:
        s = input("Give a set of numbers separated by space characters : ")
        intlist = convert_to_int_list(s.split(' '))
        if calc_action == "Sum":
            # print("Sum of list %s is %d" % (str(intlist), summate(intlist)))
            print(f"Sum of list {intlist} is {summate(intlist)}")
        elif calc_action == "Average":
            # print("Average of list %s is %f" % (str(intlist), average(intlist)))
            print(f"Average of list {intlist} is {average(intlist)}")
    except:
        print("Not a correct input for an integer list. Please try again")
        do_list_of_numbers_calculation(calc_action)

def do_calculations() -> bool:
    calc_action = input("What type of calculation do you want to do :")
    if calc_action == "Faculty":
        do_one_number_calculation(calc_action)
    elif calc_action in ("Add", "Subtract", "Multiply", "Divide"):
        do_two_number_calculation(calc_action)
    elif calc_action in {"Sum", "Average"}:
        do_list_of_numbers_calculation(calc_action)
    elif calc_action == "Quit":
        return False
    else:
        print(
            "Incorrect. Available options are "
            "'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'"
        )
    return True

continuecalcu = True
while continuecalcu:
    continuecalcu = do_calculations()
print("Thank you for user our software")

