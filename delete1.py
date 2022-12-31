import os
import mysql.connector
import sys
from tabulate import tabulate
mydb=mysql.connector.connect(user='root',passwd='',host='localhost',database='BreakOCLOCK')
mycursor=mydb.cursor(buffered=True)


def delete():
    ch='y'
    while(ch=='y'):
        print("#"*170)
        print("a)Delete from Pastries".center(170))
        print("b)Delete from Cookies".center(170))
        print("c)Delete from Breads and buns".center(170))
        print("d)Delete from Cakes".center(170))
        print("e)Delete from Coffee and tea".center(170))
        print("f) EXIT DELETE".center(170))
        f=input("Which table you want to delete a record from? a/b/c/d/e or press f to EXIT")
        
        if f=='a':
            mycursor.execute("select * from pastries")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=["Itemno","Itemname", "Description", "Status", "Price(INR)"]))
            s=input("Any records to be deleted?")
            if s=='y' or s=='Y':
                A=input("Enter the Itemno whose records are needed to be deleted")
                mycursor.execute("delete from pastries where Itemno='"+str(A)+"'" )
                mycursor.execute("delete from product where Itemno='"+str(A)+"'" )
                g=input("Are you sure, you want to delete it?")
                if g=='y' or g=='Y':
                    mydb.commit()
                    print("Record deleted :)")
            elif s=='n' or s=='N':
                continue
                
        elif f=='b':
            mycursor.execute("select * from cookies")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=["Itemno", "Itemname", "Description", "Price(INR)", "Status"]))
            s=input("Any records to be deleted?")
            if s=='y' or s=='Y':
                A=input("Enter the Itemno whose records are needed to be deleted")
                mycursor.execute("delete from cookies where Itemno='"+str(A)+"'" )
                g=input("Are you sure, you want to delete it?")
                if g=='y' or g=='Y':
                    mydb.commit()
                    print("Record deleted :)")
            elif s=='n' or s=='N':
                continue
            
        elif f=='c':
            mycursor.execute("select * from breadsandbuns")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=["Itemno", "Itemname", "Description", "Price(INR)", "Status"]))
            s=input("Any records to be deleted?")
            if s=='y' or s=='Y':
                A=input("Enter the Itemno whose records are needed to be deleted")
                mycursor.execute("delete from breadsandbuns where Itemno='"+str(A)+"'" )
                mycursor.execute("delete from product where Itemno='"+str(A)+"'" )
                g=input("Are you sure, you want to delete it?")
                if g=='y' or g=='y':
                    mydb.commit()
                    print("Record deleted :)")
            elif s=='n' or s=='N':
                continue
            
        elif f=='d':
            mycursor.execute("select * from cakes")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=["Itemno", "Itemname", "Description", "Price(INR)", "Status"]))
            s=input("Any records needed to be deleted?")
            if s=='y' or s=='Y':
                A=input("Enter the Itemno whose records are needed to be deleted")
                mycursor.execute("delete from cakes where Itemno='"+str(A)+"'" )
                mycursor.execute("delete from product where Itemno='"+str(A)+"'" )
                g=input("Arre you sure, you want to delete it?")
                if g=='y' or g=='Y':
                    mydb.commit()
                    print("Record deleted :)")
            elif s=='n' or s=='N':
                continue
                
            
        elif f=='e':
            mycursor.execute("select * from cofeeandtea")
            myrecords=mycursor.fetchall()
            print(tabulate(myrecords, headers=["Itemno", "Itemname", "Price(INR)", "Status"]))
            s=input("Any records needed to be delted?")
            if s=='y' or s=='Y':
                A=input("Enter the Itemno whose records are needed to be deleted")
                mycursor.execute("delete from cofeeandtea where Itemno='"+str(A)+"'" )
                mycursor.execute("delete from product where Itemno='"+str(A)+"'" )
                g=input("Are you sure, you want to delete it?")
                if g=='y' or g=='Y':
                    mydb.commit()
                    print("Record deleted :)")
            elif s=='n' or s=='N':
                continue

        elif f=='f':
            print("Records deleted successfully :)")
            break    
            

        r=input("Do you want to delete more records?")
        if r=='y' or r=='Y':
            continue
        elif r=='n' or r=='N':
            print("Records deleted successfully :)")
            break

        

delete()



            
