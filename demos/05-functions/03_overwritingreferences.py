def change_me2(mylist):
    """This changes a passed list into this function"""
    mylist = [1, 2, 3, 4]  # This would assign new reference
    print("Values inside the function changeme2: ", mylist)
    return


my_list_outer = [10, 20, 30]
change_me2(my_list_outer)
print("Values outside the function: ", my_list_outer)


def change_me3(my_str):
    my_str = my_str + " data inside"
    print("Values inside the function change_me3: ", my_str)
    return


my_str_outer = "data outside"
change_me3(my_str_outer)
print("Values outside the function: ", my_str_outer)
