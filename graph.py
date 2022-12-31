import mysql.connector
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="breakoclock")
mycursor=mydb.cursor()
mycursor.execute("select sum(TotPrice), Date from finalbill group by date")
myrecords=mycursor.fetchall()
date=[]
price=[]
for i in range(len(myrecords)):
    date.append(myrecords[i][0])
    price.append(myrecords[i][1])

plt.plot(price, date, marker='o')
plt.title("Daily Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
