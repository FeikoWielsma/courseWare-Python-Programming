from calcu import faculty, convertointlist, summate, average, add, subtract, multiply, divide
import sqlite3

resdict = {"Add" : [], "Subtract" : [],"Multiply" : [] ,"Divide" : []}
calcAction = "Continue"

con = sqlite3.connect('calculations.db')

with con:   
    cur = con.cursor()  
    cur.execute("DROP TABLE IF EXISTS Calculations")  
    cur.execute("CREATE TABLE Calculations(Id VARCHAR(10), Nr1 INT, Nr2 INT, Result DECIMAL)")

while (calcAction != "Quit") :
    calcAction = input ("What type of calculation do you want to do :")
    if (calcAction == "Faculty") :
        try :
            x = int(input("Give a positive integer number : "))
            print ("Faculty of %d is %d" %(x , faculty(x)))

            with con:
                cur = con.cursor()    
                cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calcAction, x, 0, faculty(x)))
        except :
            print ("Conversion to positive integer failed. Please try again")
    elif ((calcAction == "Sum") or (calcAction == "Average")) :
        try :   
            s = input("Give a set of numbers separated by space characters : ")
            intlist = convertointlist(s.split(' '))  
            if (calcAction == "Sum") :
                print ("Sum of list %s is %d" %(str(intlist), summate(intlist)))
            elif (calcAction == "Average") :   
                print ("Average of list %s is %f" %(str(intlist), average(intlist)))
        except :
            print ("Not a correct input for an integer list. Please try again")
    elif ((calcAction == "Add") or (calcAction == "Subtract") or (calcAction == "Multiply") or (calcAction == "Divide")) :    
        try :
            f1 = float(input("Give me number 1 : "))
            f2 = float(input ("Give me number 2 : "))
       
            if (calcAction == "Add") : 
                addlist = [f1, f2, add (f1, f2)]
                resdict["Add"] = resdict["Add"] + addlist
                with con:
                    cur = con.cursor()    
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calcAction, f1, f2, add(f1, f2)))
            elif (calcAction == "Subtract") : 
                subtractlist= [f1, f2, subtract (f1, f2)]
                resdict["Subtract"] = resdict["Subtract"] + subtractlist
                with con:
                    cur = con.cursor()    
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calcAction, f1, f2, subtract(f1, f2)))
            elif (calcAction == "Multiply") :
                multiplylist = [f1, f2, multiply(f1, f2)]
                resdict["Multiply"] = resdict["Multiply"] + multiplylist
                with con:
                    cur = con.cursor()    
                    cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calcAction, f1, f2, multiply(f1, f2)))
            elif (calcAction == "Divide") : 
                try :
                    dividelist = [f1, f2, divide(f1, f2)]
                    resdict["Divide"] = resdict["Divide"] + dividelist
                    with con:
                        cur = con.cursor()    
                        cur.execute("INSERT INTO Calculations ('Id', 'Nr1', 'Nr2', 'Result') VALUES(?,?,?,?)", (calcAction, f1, f2, divide(f1, f2)))

                except :
                    print ("Division by zero not allowed. Please try again") 
            print ("Content of dictionary : %s" %(resdict))
            print ("Length of dictionary : %s" %len(resdict))
        except :
            print ("Conversion of input to float failed. Please try again")
    else :
        if (calcAction!= "Quit"):
            print ("Incorrect. Available options are 'Sum', 'Average', 'Add', 'Subtract, 'Multiply, 'Divide'")
else :
    print ("Thank you for user our software")
