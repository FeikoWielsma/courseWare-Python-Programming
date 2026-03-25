reslist = []
multireslist = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#step 1
while True :
    f1 = float(input("Give me number 1 : "))
    f2 = float(input ("Give me number 2 : "))

    addresult = f1 + f2
    reslist.append(f1)
    reslist.append(f2)
    reslist.append(addresult)
    #print("Content of list %s : " %(reslist))
    #print("Length of list %s : " %len(reslist))
    #print("Part of list %s : " % reslist[0:3])
    print(f"Content of list {reslist} : ")
    print(f"Length of list {len(reslist)}: ")
    print(f"Part of list {reslist[0:3]} : ")

    print(reslist[0])
    del reslist[0]
    # print("Content of list after deletion %s : " %(reslist))
    print(f"Content of list after deletion {reslist} : ")
    
#step 2
# while True :
#    f1 = float(input("Give me number 1 : "))
#    f2 = float(input ("Give me number 2 : "))
#    addresult = f1 + f2
#    # addlist = ("Add", f1, f2, addresult)
#    addlist = ["Add", f1, f2, addresult]
#    multireslist[0] = addlist
#
#    subtractresult = f1 - f2
#    subtractlist= ["Subtract", f1, f2, subtractresult]
#    multireslist[1]= subtractlist
#
#    multiplyresult = f1 * f2
#    multiplylist = ["Multiply", f1, f2, multiplyresult]
#    multireslist[2] = multiplylist
#
#    divideresult = f1 / f2
#    dividelist = ["Divide", f1, f2, divideresult]
#    multireslist[3] = dividelist
#
#    # print("Content of list : %s" %(multireslist))
#    # print("Length of list : %s" %len(multireslist[0]))
#    print(f"Content of list : {multireslist}")
#    print(f"Length of list : {len(multireslist[0])}")
#
#    multireslist[1][1] = None
#    multireslist[0][1] = None
#    # print("Content of list : %s" %(multireslist))
#    print(f"Content of list : {multireslist}")

#step 3
# resdict = {}
# resdict = {"Add": [], "Subtract": [], "Multiply": [], "Divide": []}
# while True:
#     f1 = float(input("Give me number 1 : "))
#     f2 = float(input("Give me number 2 : "))
#
#     addresult = f1 + f2
#     addlist = [f1, f2, addresult]
#     resdict["Add"] = resdict["Add"] + addlist
#
#     subtractresult = f1 - f2
#     subtractlist= [f1, f2, subtractresult]
#     resdict["Subtract"] = resdict["Subtract"] + subtractlist
#
#     multiplyresult = f1 * f2
#     multiplylist = [f1, f2, multiplyresult]
#     resdict["Multiply"] = resdict["Multiply"] + multiplylist
#
#     divideresult = f1 / f2
#     dividelist = [f1, f2, divideresult]
#     resdict["Divide"] = resdict["Divide"] + dividelist
#
#     # print("Content of dictionary : %s" %(resdict))
#     # print("Length of dictionary : %s" %len(resdict))
#     print(f"Content of dictionary : {resdict}")
#     print(f"Length of dictionary : {len(resdict)}")
#
#     resdict["Divide"] = resdict["Divide"] + [1, 0, "Infinite"]
#     #print("Content of dictionary : %s" %(resdict))
#     print(f"Content of dictionary : {resdict}")

#step 4
# while True :
#     s = input("Give me a set of numbers separated by space characters : ")
#     slist = s.split(' ')
#     print(slist)
#
#     slist.sort()
#     print(slist)
#
#     slist.reverse()
#     print(slist)
#
#     intlist = []
#
#     for x in slist:
#         x = int(x)
#         intlist.append(x)
#
#     print(intlist)