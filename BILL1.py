import mysql.connector
from tabulate import tabulate
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="breakoclock")
mycursor=mydb.cursor()
def purchase():
    ch="y"
    while(ch=="y"):
        print("")
        print("MENU".center(170))
        print(" ")
        print(" ")

        print("PASTRIES")
        print("")
        mycursor.execute("select * from pastries")
        myrecords=mycursor.fetchall()
        print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Status", "Price(INR)"]))
        print("")
        
        print("COOKIES")
        print("")
        mycursor.execute("select * from cookies")
        myrecords=mycursor.fetchall()
        print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
        print("")
        
        print("BREADS AND BUNS")
        print("")
        mycursor.execute("select * from breadsandbuns")
        myrecords=mycursor.fetchall()
        print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
        print("")
        
        print("CAKES")
        print("")
        mycursor.execute("select * from cakes")
        myrecords=mycursor.fetchall()
        print(tabulate(myrecords,headers=["Itemno","Itemname", "Description", "Price(INR)", "Status"]))
        print("")
        
        print("COFFEE AND TEA")
        print("")
        mycursor.execute("select * from cofeeandtea")
        myrecords=mycursor.fetchall()
        print(tabulate(myrecords,headers=["Itemno","Itemname", "Price(INR)", "Status"]))
        print("")
        
        print(" ")
        print(" ")
        g=input("Welcome :) would you like to make a purchase(Y/N)")
        if g=='y' or g=='Y':
            productid=int(input("WELCOME:)WHAT WOULD YOU LIKE TO HAVE TODAY, SEEMS MOUTH-WATERING(enter product id):"))
            mycursor.execute("select * from product where Itemno ='"+str(productid)+"'")
            myrecords1=mycursor.fetchall()
            print(myrecords1)
            pi=myrecords1[0][0]
            pm=myrecords1[0][1]
            cs=myrecords1[0][2]
            mycursor.execute("insert into bill1 values('"+str(pi)+"','"+str(pm)+"','"+str(cs)+"')")
            ch=input("WANT TO PURCHASE MORE OF THEM :)) SOMETHING IS SURELY UP YOUR MIND(Y/N)")
            if ch=="y":
                continue
            elif ch=="n":
                mycursor.execute("select * from bill1")
                myrecords2=mycursor.fetchall()
                print(tabulate(myrecords2,headers=["Itemno", "Itenmane", "PriceINR"]))
                tot=0
                for i in myrecords2:
                    tot+=1
        elif g=='n' or g=='N':
            print("Thank you for coming! Have a nice day :)")
            break

        
    else:
        ques2=int(input("PRESS 1 TO RECEICE YOUR BILL :D"))
        if ques2==1:
            mobile_number=int(input("ENTER CUSTOMER MOBILE NUMBER:"))
            customer_name=input("ENTER CUSTOMER NAME:")
            x=input("TODAY'S DATE(YY-MM-DD)")
            print(" ")
            mycursor.execute("select * from bill1")
            myrecords2=mycursor.fetchall()
            totprice=0
            for i in range(len(myrecords2)):
                    totprice+=myrecords2[i][2]
            mycursor.execute("delete from bill1")
            mycursor.execute("insert into finalbill values('"+str(mobile_number)+"','"+(customer_name)+"','"+str(tot)+"','"+str(totprice)+"','"+str(x)+"')")
            mydb.commit()
            print("")
            print("*"*170)
            print("HERE'S YOUR BILL :)) ENJOY '"+str(customer_name)+"'".center(170))
            print(tabulate(myrecords2,headers=["Itemno", "Itenmane", "PriceINR"]))
            print("")
            print("YOUR BILL IS",totprice)
            print("THANK YOU! COME AGAIN, HAVE A NICE DAY :)".center(170))
            print("*"*170)
            
            print(" ")
                         
purchase()
