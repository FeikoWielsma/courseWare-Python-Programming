def change_me1(mylist: list[int]) -> None:
    """This function changes a passed list and the list is changed outside the function as well"""
    mylist.append(40)
    print("List inside the function change_me1: ", mylist)


my_list_outer = [10, 20, 30]
change_me1(my_list_outer)
print("List outside the function: ", my_list_outer)
