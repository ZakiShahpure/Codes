import mysql.connector as mycon
con = mycon.connect(host='127.0.0.1',user='root',password="Fmi#123@123$")
cur = con.cursor()
cur.execute("use company")
con.commit()
choice=None
while choice!=0:
    print("1. SEARCH RECORD ")
    print("2. DISPLAY RECORD ")
    print("0. EXIT")
    choice = int(input("Enter Choice :"))
    if choice == 1:
        eno = int(input("ENTER EMPNO TO SEARCH :"))
        query = "select * from google where empno={}".format(eno)
        cur.execute(query)
        result = cur.fetchall()
        if cur.rowcount == 0:
            print("Sorry! Empno not found ")
        else:
            print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT",
                  "%10s" % "SALARY")
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])
        ans = input("SEARCH MORE (Y) :")

