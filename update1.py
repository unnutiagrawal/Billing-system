import os
import mysql.connector
import sys
from tabulate import tabulate
mydb=mysql.connector.connect(user='root',passwd='',host='localhost',database='BreakOCLOCK')
mycursor=mydb.cursor(buffered=True)
        


def update_pastries():
    mycursor.execute("select * from pastries")
    myrecords=mycursor.fetchall()
    print(tabulate(myrecords, headers=["Itemno","Itemname", "Description", "Status", "Price(INR)"]))
    s=input("Do you want to update records?")
    if s=='y' or s=='Y':
        A=int(input("Enter the itemno whose details needed to be updated"))
        ch=input("Change Itemname(Y/N)")
        if ch=="y" or ch=="Y":
            name=input("Enter Itemname")
            mycursor.execute("update pastries set itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set Itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
        ch=input("Change Description(Y/N)")
        if ch=="y" or ch=="Y":
            description=input("Enter Description")
            mycursor.execute("update pastries set Description='"+str(description)+"'where Itemno='"+str(A)+"'")
        ch=input("Change status(Y/N)")
        if ch=="y" or ch=="Y":
            status=input("Enter status")
            mycursor.execute("update pastries set Status='"+str(status)+"'where Itemno='"+str(A)+"'")
        ch=input("Change PriceINR(Y/N)")
        if ch=="y" or ch=="Y":
            price=float(input("Enter PriceINR"))
            mycursor.execute("update pastries set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
        mydb.commit()
        print("Record updated")
        
    

def update_cookies():
    mycursor.execute("select * from cookies")
    myrecords=mycursor.fetchall()
    print(tabulate(myrecords, headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
    s=input("Do you want to update records?")
    if s=='y' or s=='Y':
        A=int(input("Enter the itemno whose details needed to be updated"))
        ch=input("Change Itemname(Y/N)")
        if ch=="y" or ch=="Y":
            name=input("Enter Itemname")
            mycursor.execute("update cookies set itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set Itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
        ch=input("Change Description(Y/N)")
        if ch=="y" or ch=="Y":
            description=input("Enter Description")
            mycursor.execute("update cookies set Description='"+str(description)+"'where Itemno='"+str(A)+"'")
        ch=input("Change status(Y/N)")
        if ch=="y" or ch=="Y":
            status=input("Enter status")
            mycursor.execute("update cookies set Status='"+str(status)+"'where Itemno='"+str(A)+"'")
        ch=input("Change PriceINR(Y/N)")
        if ch=="y" or ch=="Y":
            price=float(input("Enter PriceINR"))
            mycursor.execute("update cookies set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
        mydb.commit()
        print("Record updated")
        
    

def update_breadandbuns():
    mycursor.execute("select * from breadsandbuns")
    myrecords=mycursor.fetchall()
    print(tabulate(myrecords, headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
    s=input("Do you want to update records?")
    if s=='y' or s=='Y':
        A=int(input("Enter the itemno whose details needed to be updated"))
        ch=input("Change Itemname(Y/N)")
        if ch=="y" or ch=="Y":
            name=input("Enter Itemname")
            mycursor.execute("update breadsandbuns set itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set Itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
        ch=input("Change Description(Y/N)")
        if ch=="y" or ch=="Y":
            description=input("Enter Description")
            mycursor.execute("update breadsandbuns set Description='"+str(description)+"'where Itemno='"+str(A)+"'")
        ch=input("Change status(Y/N)")
        if ch=="y" or ch=="Y":
            status=input("Enter status")
            mycursor.execute("update breadsandbuns set Status='"+str(status)+"'where Itemno='"+str(A)+"'")
        ch=input("Change PriceINR(Y/N)")
        if ch=="y" or ch=="Y":
            price=float(input("Enter PriceINR"))
            mycursor.execute("update breadsandbuns set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
        mydb.commit()
        print("Record updated")
            
    

def update_cakes():
    mycursor.execute("select * from cakes")
    myrecords=mycursor.fetchall()
    print(tabulate(myrecords, headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
    s=input("Do you want to update records?")
    if s=='y' or s=='Y':
        A=int(input("Enter the itemno whose details needed to be updated"))
        ch=input("Change Itemname(Y/N)")
        if ch=="y" or ch=="Y":
            name=input("Enter Itemname")
            mycursor.execute("update cakes set itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set Itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
        ch=input("Change Description(Y/N)")
        if ch=="y" or ch=="Y":
            description=input("Enter Description")
            mycursor.execute("update cakes set Description='"+str(description)+"'where Itemno='"+str(A)+"'")
        ch=input("Change status(Y/N)")
        if ch=="y" or ch=="Y":
            status=input("Enter status")
            mycursor.execute("update cakes set Status='"+str(status)+"'where Itemno='"+str(A)+"'")
        ch=input("Change PriceINR(Y/N)")
        if ch=="y" or ch=="Y":
            price=float(input("Enter PriceINR"))
            mycursor.execute("update cakes set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
        mydb.commit()
        print("Record updated")
    


        
def update_coffeeandtea():
    mycursor.execute("select * from cofeeandtea")
    myrecords=mycursor.fetchall()
    print(tabulate(myrecords, headers=["Itemno","Itemname", "Price(INR)", "Status"]))
    s=input("Do you want to update records?")
    if s=='y' or s=='Y':
        A=int(input("Enter the itemno whose details needed to be updated"))
        ch=input("Change Itemname(Y/N)")
        if ch=="y" or ch=="Y":
            name=input("Enter Itemname")
            mycursor.execute("update cofeeandtea set itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set Itemname='"+str(name)+"'where Itemno='"+str(A)+"'")
        ch=input("Change status(Y/N)")
        if ch=="y" or ch=="Y":
            status=input("Enter status")
            mycursor.execute("update cofeeandtea set Status='"+str(status)+"'where Itemno='"+str(A)+"'")
        ch=input("Change PriceINR(Y/N)")
        if ch=="y" or ch=="Y":
            price=float(input("Enter PriceINR"))
            mycursor.execute("update cofeeandtea set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
            mycursor.execute("update product set PriceINR='"+str(price)+"'where Itemno='"+str(A)+"'")
        mydb.commit()
        print("Record updated")
        
    
    
def update():
    ch='y'
    while(ch=='y'):
        print("#"*170)
        print("a)Update Pastries".center(170))
        print("b)Update Cookies".center(170))
        print("c)Update Breads and buns".center(170))
        print("d)Update Cakes".center(170))
        print("e)Update Coffee and tea".center(170))
        print("f) EXIT UPDATE".center(170))
        d=input("Which table you choose to update? a/b/c/d/e or press f to EXIT")

        if d=='a':
            update_pastries()
        elif d=='b':
            update_cookies()
        elif d=='c':
            update_breadandbuns()
        elif d=='d':
            update_cakes()
        elif d=='e':
            update_coffeeandtea()
        elif d=='f':
            break

        r=input("Do you want to update any more records?")
        if r=='y' or r=='Y':
            continue
        elif r=='n' or r=='N':
            print("Record updated successfully")
            break

update()
