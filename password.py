import os
import mysql.connector
import sys
from easygui import passwordbox

mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="student")
mycursor=mydb.cursor()

password=passwordbox("Enter password")
name=input("enter your name")
print("")
print("")
if password=="#Eatingout":
    print("Hey,", name)
else:
    print("Sorry, try again",name)
    sys.exit()
