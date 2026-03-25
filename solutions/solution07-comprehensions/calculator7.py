from functools import reduce

resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
calcAction = "Continue"
while calcAction != "Quit":
    calcAction = input ("What type of calculation do you want to do :")
    if calcAction == "Faculty":
        n = int(input("Give a positive integer number : "))
        fac = reduce((lambda x, y : x * y), list(range(1, n+1)))
        # print("Faculty of %d is %d" %(n , fac))
        print(f"Faculty of {n} is {fac}")
    elif (calcAction == "Sum") or (calcAction == "Average"):
        s = input("Give a set of numbers separated by space characters : ")
        slist = s.split(' ')
        intlist = [int(s) for s in slist]
        if calcAction == "Sum":
            summation = reduce((lambda x, y: x + y), intlist)
            # print("Sum of list %s is %d" %(str(intlist), summation))
            print(f"Sum of list {intlist} is {summation}")
        elif calcAction == "Average":
            av = reduce((lambda x, y: x + y), intlist)/len(intlist)
            # print("Average of list %s is %f" %(str(intlist), av))
            print(f"Average of list {intlist} is {av}")
    elif (calcAction == "Add") or (calcAction == "Subtract") or (calcAction == "Multiply") or (calcAction == "Divide"):
        f1 = float(input("Give me number 1 : "))
        f2 = float(input("Give me number 2 : "))
        if calcAction == "Add":
            resdict["Add"] = resdict["Add"] + [f1, f2, (lambda x, y: x + y)(f1, f2)]
        elif calcAction == "Subtract":
            resdict["Subtract"] = resdict["Subtract"] + [f1, f2, (lambda x, y: x - y)(f1, f2)]
        elif calcAction == "Multiply":
            resdict["Multiply"] = resdict["Multiply"] + [f1, f2, (lambda x, y: x * y)(f1, f2)]
        elif calcAction == "Divide":
            resdict["Divide"] = resdict["Divide"] + [f1, f2, (lambda x, y: x / y)(f1, f2)]
        # print("Content of dictionary : %s" %(resdict))
        # print("Length of dictionary : %s" %len(resdict))
        print(f"Content of dictionary : {resdict}")
        print(f"Length of dictionary : {len(resdict)}")
    else:
        if calcAction != "Quit":
            print("Incorrect. Available options are 'Faculty', 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
else:
    print("Thank you for user our software")

