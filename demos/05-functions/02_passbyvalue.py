def changeme1(mylist):
    """This function changes a passed list and the list is changed outside the function as well"""
    mylist.append(40)
    print("List inside the function changeme1: ", mylist)
    return

mylistouter = [10,20,30]
changeme1(mylistouter)
print("List outside the function: ", mylistouter)



