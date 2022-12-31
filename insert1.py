import os
import mysql.connector
import sys
from tabulate import tabulate
mydb=mysql.connector.connect(user='root',passwd='',host='localhost',database='BreakOCLOCK')
mycursor=mydb.cursor(buffered=True)




def insert():
    ch='y'
    while(ch=='y'):
        
        print("a)Insert into Pastries".center(170))
        print("b)Insert into Cookies".center(170))
        print("c)Insert into Breads and buns".center(170))
        print("d)Insert into Cakes".center(170))
        print("e)Insert into Coffee and tea".center(170))
        print("f)EXIT INSERT".center(170))
        
        w=input("Which table you want to insert a record in? a/b/c/d/e or press f to EXIT")

        
        if w=='a':
            
            print("PASTRIES")
            print("")
            mycursor.execute("select * from pastries")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Status", "Price(INR)"]))
            print("")
            s=input("Do you want to insert records?")
            if s=='y' or s=='Y':
                Itemno=input("Enter itemno")
                Itemname=input("Enter Item name")
                Description=input("Enter Description")
                Status=input("Enter status")
                Price=int(input("Enter PriceINR"))
                Rec=[Itemno, Itemname, Description, Status, Price]
                cmd="insert into pastries values(%s, %s, %s, %s, %s)"
                mycursor.execute(cmd, Rec)
                Rec2=[Itemno, Itemname, Price]
                cmd2="insert into product values(%s,%s,%s)"
                mycursor.execute(cmd2, Rec2)
                mydb.commit()

        elif w=='b':
            print("COOKIES")
            print("")
            mycursor.execute("select * from cookies")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
            print("")
            s=input("Do you want to insert Records?")
            if s=='y' or s=='Y':
                Itemno=input("Enter itemno")
                Itemname=input("Enter Item name")
                Description=input("Enter Description")
                Price=int(input("Enter PriceINR"))
                Status=input("Enter Status")
                Rec=[Itemno, Itemname, Description, Price, Status]
                cmd="insert into cookies values(%s, %s, %s, %s, %s)"
                mycursor.execute(cmd, Rec)
                Rec2=[Itemno, Itemname, Price]
                cmd2="insert into product values(%s,%s,%s)"
                mycursor.execute(cmd2, Rec2)
                mydb.commit()
                        
        elif w=='c':
            print("BREADS AND BUNS")
            print("")
            mycursor.execute("select * from breadsandbuns")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
            print("")
            s=input("Do you want to insert records?")
            if s=='y' or s=='Y':
                Itemno=input("Enter itemno")
                Itemname=input("Enter Item name")
                Description=input("Enter Description")
                Status=input("Enter status")
                Price=int(input("Enter PriceINR"))
                Rec=[Itemno, Itemname, Description, Price, Status]
                cmd="insert into breadsandbuns values(%s, %s, %s, %s, %s)"
                mycursor.execute(cmd, Rec)
                Rec2=[Itemno, Itemname, Price]
                cmd2="insert into product values(%s,%s,%s)"
                mycursor.execute(cmd2, Rec2)
                mydb.commit()
                
            
                        
        elif w=='d':
            print("CAKES")
            print("")
            mycursor.execute("select * from cakes")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
            print("")
            s=input("Do you want to insert records?")
            if s=='y' or s=='Y':
                Itemno=input("Enter itemno")
                Itemname=input("Enter Item name")
                Description=input("Enter Description")
                Status=input("Enter status")
                Price=int(input("Enter PriceINR"))
                Rec=[Itemno, Itemname, Description, Price, Status]
                cmd="insert into cakes values(%s, %s, %s, %s, %s)"
                Rec2=[Itemno, Itemname, Price]
                cmd2="insert into product values(%s,%s,%s)"
                mycursor.execute(cmd2, Rec2)
                mycursor.execute(cmd, Rec)
                mydb.commit()
                        
        elif w=='e':
            print("COFFEE AND TEA")
            print("")
            mycursor.execute("select * from cofeeandtea")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords,headers=["Itemno","Itemname", "Price(INR)", "Status"]))
            print("")
            s=input("Do you want to insert records?")
            if s=='y' or s=='Y':
                Itemno=input("Enter itemno")
                Itemname=input("Enter Item name")
                Status=input("Enter status")
                Price=float(input("Enter PriceINR"))
                Rec=[Itemno, Itemname, Price, Status]
                cmd ="insert into cofeeandtea values(%s, %s, %s, %s)"
                mycursor.execute(cmd, Rec)
                Rec2=[Itemno, Itemname, Price]
                cmd2="insert into product values(%s,%s,%s)"
                mycursor.execute(cmd2, Rec2)
                mydb.commit()
        elif w=='f':
            break
                
                
            
                
        r=input("Do you want to insert records in another table?")
        if r=='y' or r=='Y':
            continue
        elif r=='n' or r=='N':
            print("Records inserted successfully")
            break
insert()
