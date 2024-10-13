#create db connection and add new database and check that database added into database list or not .
import mysql.connector as mycon
con = mycon.connect()
try:
    # Create a MySQL connection
    con = mycon.connect(host='127.0.0.1', user='root', password='root')

    if con.is_connected():
        print("Database connected successfully")

    # Create a cursor to interact with the database
    cur = con.cursor()

    # Create a new database (replace 'new_database' with your desired database name)
    new_database_name = input("Enter database name to be created: ")
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {new_database_name}")
    print(f"{new_database_name} database is created successfully ..")

    # Display all databases
    cur.execute("SHOW DATABASES")
    # Fetch and print the list of databases
    print("List of all database")
    databases = cur.fetchall()
    for database in databases:
        print(database[0])

except:
    print("Data connection failed ...check database id password")

finally:
    # Close the database connection in the 'finally' block to ensure it's closed regardless of exceptions
    con.close()
    