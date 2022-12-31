import os
import mysql.connector
import sys
from tabulate import tabulate
mydb=mysql.connector.connect(user='root',passwd='',host='localhost',database='BreakOCLOCK')
mycursor=mydb.cursor(buffered=True)



while True:
    print("="*170)
    print("1) Update a record".center(170))
    print("2) Insert a new record".center(170))
    print("3) Delete an existing record".center(170))
    print("4) Develop graph for the bakery on daily basis".center(170))
    print("5) Exit seller table".center(170))
    d=int(input("What would you like to choose"))
    if d==1:
        import update1
    elif d==2:
        import insert1
    elif d==3:
        import delete1
    elif d==4:
        import graph
    elif d==5:
        break
    
