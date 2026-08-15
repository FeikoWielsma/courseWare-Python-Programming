#step1
def add(i: float, j: float) -> float:
    return i + j

def subtract(i: float, j: float) -> float:
    return i - j

def multiply(i: float, j: float) -> float:
    return i * j

def divide(i: float, j: float) -> float:
    return i / j

#step2
def convert_to_int_list(slist: list[str]) -> list[int]:
    ilist = []
    for x in slist:
        ilist.append(int(x))
    return ilist

def summate(ilist: list[int]) -> int:
    s = 0
    for x in ilist:
        s = s + x
    return s

def average(ilist: list[int]) -> float:
    s = 0
    for x in ilist:
        s = s + x
    return s / len(ilist)

#step3
def faculty(n: int) -> int:
    if n == 1:
        return n
    return n*faculty(n-1)

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
calc_action = "Continue"
while calc_action != "Quit":
    calc_action = input ("What type of calculation do you want to do :")
    if calc_action == "Faculty":
        x = int(input("Give a positive integer number : "))
        fac = faculty(x)
        #print("Faculty of %d is %d" %(x , fac))
        print(f"Faculty of {x} is {fac}")
    elif calc_action in {"Sum", "Average"}:
        s = input("Give a set of numbers separated by space characters : ")
        slist = s.split(' ')
        intlist = convert_to_int_list(slist)
        if calc_action == "Sum":
            summation = summate(intlist)
            #print ("Sum of list %s is %d" %(str(intlist), summation))
            print(f"Sum of list {intlist} is {summation}")
        elif calc_action == "Average":
            av = average(intlist)
            #print ("Average of list %s is %f" %(str(intlist), av))
            print(f"Average of list {intlist} is {av}")
    elif calc_action in ("Add", "Subtract", "Multiply", "Divide"):
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calc_action == "Add":
            addresult = add(f1, f2)
            addlist = [f1, f2, addresult]
            resdict["Add"] = resdict["Add"] + addlist
        elif calc_action == "Subtract":
            subtractresult = subtract (f1, f2)
            subtractlist= [f1, f2, subtractresult]
            resdict["Subtract"] = resdict["Subtract"] + subtractlist
        elif calc_action == "Multiply":
            multiplyresult = multiply(f1, f2)
            multiplylist = [f1, f2, multiplyresult]
            resdict["Multiply"] = resdict["Multiply"] + multiplylist
        elif calc_action == "Divide":
            divideresult = divide(f1, f2)
            dividelist = [f1, f2, divideresult]
            resdict["Divide"] = resdict["Divide"] + dividelist
        # print("Content of dictionary : %s" %(resdict))
        # print("Length of dictionary : %s" %len(resdict))
        print(f"Content of dictionary : {resdict}")
        print(f"Length of dictionary : {len(resdict)}")
    else:
        if calc_action != "Quit":
            print(
                "Incorrect. Available options are "
                "'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'"
            )
print("Thank you for user our software")
