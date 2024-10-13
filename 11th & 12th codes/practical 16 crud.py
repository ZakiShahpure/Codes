import mysql.connector as mycon

# Create a MySQL connection
con = mycon.connect(host='127.0.0.1', user='root', password="root")

# Create a cursor to interact with the database
cur = con.cursor()

# Create the 'company' database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS company")

# Switch to the 'company' database
cur.execute("USE company")

# Create the 'employee' table if it doesn't exist with 'empno' as the primary key
cur.execute("CREATE TABLE IF NOT EXISTS google(empno int PRIMARY KEY, name varchar(20), dept varchar(20), salary int)")

# Commit the changes
con.commit()

choice = None

while choice != 0:
    print("1. ADD RECORD ")
    print("2. UPDATE RECORD ")
    print("3. DELETE RECORD ")
    print("4. DISPLAY RECORD ")
    print("5. SEARCH RECORD ")
    print("0. EXIT")
    choice = int(input("Enter Choice :"))

    if choice == 1:
        e = int(input("Enter Employee Number: "))
        n = input("Enter Name: ")
        d = input("Enter Department: ")
        s = int(input("Enter Salary: "))

        try:
            # Insert a new record into the 'employee' table
            query = "INSERT INTO google VALUES({},'{}','{}',{})".format(e, n, d, s)
            cur.execute(query)
            print(" D a t a   S a v e d ")
        except:
            print("duplicate employee number check and give valid emp-number ")
        # Commit the changes to the database
        con.commit()


    elif choice == 2:
        empno_to_update = int(input("Enter Employee Number to Update: "))
        n = input("Enter New Name: ")
        d = input("Enter New Department: ")
        s = int(input("Enter New Salary: "))

        # Update an existing record in the 'employee' table
        query = "UPDATE google SET name='{}', dept='{}', salary={} WHERE empno={}".format(n, d, s,empno_to_update)
        cur.execute(query)

        # Commit the changes to the database
        con.commit()

        print(" D a t a   U p d a t e d ")

    elif choice == 3:
        empno_to_delete = int(input("Enter Employee Number to Delete: "))

        # Delete the record with the specified empno from the 'employee' table
        query = "DELETE FROM google WHERE empno = {}".format(empno_to_delete)
        cur.execute(query)

        # Commit the changes to the database
        con.commit()

        print(" D a t a   D e l e t e d ")


    elif choice == 4:
         # Retrieve and display all records from the 'employee' table
        query = "SELECT * FROM google"
        cur.execute(query)
        result = cur.fetchall()

        # Display the header row
        print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT", "%10s" % "SALARY")

        # Display the data rows
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])

    elif choice == 5:
        eno = int(input("ENTER EMPNO TO SEARCH :"))
        query = "select * from google where empno={}".format(eno)
        cur.execute(query)
        result = cur.fetchall()
        if cur.rowcount == 0:
            print("S o r r y ! Empno not found ")
        else:
            print("Record found ")
            print("%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT",
                  "%10s" % "SALARY")
        for row in result:
            print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])

    elif choice == 0:
        # Close the database connection
        con.close()
        print(" D A T A B A S E    C  L O S E . . .")

    else:
        print(" I N V A L I D   C H O I C E  ")
