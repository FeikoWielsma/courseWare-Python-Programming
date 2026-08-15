import sqlite3

from calcu import add, average, convert_to_int_list, divide, faculty, multiply, subtract, summate

resdict = {"Add" : [], "Subtract" : [],"Multiply" : [] ,"Divide" : []}
calc_action = "Continue"

con = sqlite3.connect('calculations.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Calculations")
    cur.execute("CREATE TABLE Calculations(Id VARCHAR(10), Nr1 INT, Nr2 INT, Result DECIMAL)")

while (calc_action != "Quit") :
    calc_action = input ("What type of calculation do you want to do :")
    if (calc_action == "Faculty") :
        try :
            x = int(input("Give a positive integer number : "))
            print(f"Faculty of {x} is {faculty(x)}")

            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calc_action, x, 0, faculty(x)))
        except ValueError:
            print ("Conversion to positive integer failed. Please try again")
    elif ((calc_action == "Sum") or (calc_action == "Average")) :
        try :
            s = input("Give a set of numbers separated by space characters : ")
            intlist = convert_to_int_list(s.split(' '))
            if (calc_action == "Sum") :
                print(f"Sum of list {intlist} is {summate(intlist)}")
            elif (calc_action == "Average") :
                print (f"Average of list {str(intlist)} is {average(intlist):f}")
        except ValueError:
            print ("Not a correct input for an integer list. Please try again")
    elif ((calc_action == "Add") or (calc_action == "Subtract") or (calc_action == "Multiply") or (calc_action == "Divide")) :
        try :
            f1 = float(input("Give me number 1 : "))
            f2 = float(input ("Give me number 2 : "))

            if (calc_action == "Add") :
                addlist = [f1, f2, add (f1, f2)]
                resdict["Add"] = resdict["Add"] + addlist
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calc_action, f1, f2, add(f1, f2)))
            elif (calc_action == "Subtract") :
                subtractlist= [f1, f2, subtract (f1, f2)]
                resdict["Subtract"] = resdict["Subtract"] + subtractlist
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calc_action, f1, f2, subtract(f1, f2)))
            elif (calc_action == "Multiply") :
                multiplylist = [f1, f2, multiply(f1, f2)]
                resdict["Multiply"] = resdict["Multiply"] + multiplylist
                with con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calc_action, f1, f2, multiply(f1, f2)))
            elif (calc_action == "Divide") :
                try :
                    dividelist = [f1, f2, divide(f1, f2)]
                    resdict["Divide"] = resdict["Divide"] + dividelist
                    with con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calc_action, f1, f2, divide(f1, f2)))

                except ZeroDivisionError:
                    print ("Division by zero not allowed. Please try again")
            print (f"Content of dictionary : {resdict}")
            print (f"Length of dictionary : {len(resdict)}")
        except ValueError:
            print ("Conversion of input to float failed. Please try again")
    else :
        if (calc_action!= "Quit"):
            print ("Incorrect. Available options are 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
print ("Thank you for user our software")
