#create database if not exist and create table add record and display record
import mysql.connector as mycon

con = mycon.connect(host='127.0.0.1',user='root',password="Fmi#123@123$")
cur = con.cursor()
cur.execute("create database if not exists company")
cur.execute("use company")
cur.execute("create table if not exists google(empno int PRIMARY KEY, name varchar(20), dept varchar(20),salary int)")
con.commit()
choice=None
while choice!=0:
    print("1. ADD RECORD ")
    print("2. DISPLAY RECORD ")
    print("0. EXIT")
    choice = int(input("Enter Choice :"))
    if choice == 1:
        e = int(input("Enter Employee Number :"))
        n = input("Enter Name :")
        d = input("Enter Department :")
        s = int(input("Enter Salary :"))
        query="insert into google values({},'{}','{}',{})".format(e,n,d,s)
        cur.execute(query)
        con.commit()
        print(" D A T A  S A V E D . . .")
    elif choice == 2:
        query="select * from google"
        cur.execute(query)
        result = cur.fetchall()
        print("%10s"%"EMPNO","%20s"%"NAME","%15s"%"DEPARTMENT",
        "%10s"%"SALARY")
        for row in result:
            print("%10s"%row[0],"%20s"%row[1],"%15s"%row[2],"%10s"%row[3])
    elif choice==0:
        con.close()
        print(" D A T A B A S E    C  L O S E . . .")
    else:
        print("I N V A L I D  C H O I C E . . . ")
