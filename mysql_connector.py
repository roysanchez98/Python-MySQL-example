import mysql.connector
from mysql.connector import errorcode


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="@Gumble14",
        database="empdb"  # Pass in database created

    )
    print("It works!")
    mycursor = mydb.cursor()
    # mycursor.execute("Create database empdb")  # Created database empdb

    mycursor.execute("show databases")

    for db in mycursor:
        print("Database: ", db)

    # mycursor.execute("Create table employee(name varchar(200), sal int(20))")  # Create a new table

    mycursor.execute("Show tables")

    for tb in mycursor:
        print("Table: ", tb)

    sqlform = "INSERT INTO employee(name, sal) VALUES (%s, %s)"

    employees = [("roy", 20000), ("bob", 22000), ("rem", 23000), ]

    mycursor.executemany(sqlform, employees)  # execute many because we are using a tuple


    # sql = "DELETE FROM employee WHERE name='roy'" #delete one employee at a time
    # mycursor.execute(sql)

    mydb.commit()

    mycursor.execute("Select * from employee")

    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DataBase does not exist")
    else:
        print(err)




'''
addName = "INSERT INTO Name (fName, lName) VALUES (%s, %s)"
fName = "Ray"
lName = "Donavan"
empName = (fName, lName)
mycursor.execute(addName, empName)

mydb.commit()
mycursor.close()
mydb.close
'''
