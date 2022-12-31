import os
import mysql.connector
import sys
from tabulate import tabulate
from easygui import passwordbox
mydb=mysql.connector.connect(user='root',passwd='',host='localhost',database='BreakOCLOCK')
mycursor=mydb.cursor(buffered=True)

password=passwordbox("Enter password:")


name=input("Enter your name:")
print("")
print("")
if password=="#eatout":
    print("HEY",name)
else:
    print("Sorry, Try again",name)
    sys.exit()

print("="*167)
print("/"*167)
print("*"*167)
print("Break O'Clock".center(167))
print("*"*167)
print("/"*167)

while True:
    print("How you choose to proceed?")
    print("")
    print("1. Seller Database")
    print("2. Customer Database")
    print("3. EXIT this system")
    print("")
    dis=int(input("Enter a choice from above:"))
    if dis==1:
        password=passwordbox("Enter password:")
        if password=="codeXaccess2":
            print("")
            print("Welcome, you can now see the seller records :)")
            import seller
        else:
            print("Sorry, Try again",name)
            sys.exit()         
                
    elif dis==2:
        import BILL1

    elif dis==3:
        break

        
        

