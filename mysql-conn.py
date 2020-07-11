import mysql.connector

mydb = mysql.connector.connect(  # Connection to DB (using minikube ip)
    host="192.168.99.101",
    port="31515"
)

mydbCursor = mydb.cursor()
"""
print("------------------BEFORE DATABASE CREATION------------------")
mydbCursor.execute("SHOW DATABASES")

for db in mydbCursor:
    print(db)

mydbCursor.execute("create database testdb")

print("------------------AFTER DATABASE CREATION------------------")
mydbCursor.execute("SHOW DATABASES")

for db in mydbCursor:
    print(db)

mydbCursor.execute("drop database test")
sqlQuery=mydbCursor.execute("CREATE TABlE students (name VARCHAR(255), age INT(10))")

mydbCursor.execute("SHOW TABLES")
for tb in mydbCursor:
    print(tb)
"""
mydbCursor.execute("create database testdb")
sqlQuery2 = "INSERT INTO students (name, age) VALUES (%s, %s)"  
# %s act as PLACEHOLDERS to be populated from entries in the students list object
students = [("Bob", 25),
            ("Micahel", 27),
            ("Lincoln", 32),
            ("LJ", 16),
            ("Sara", 29)]
for studs in students:
    mydbCursor.execute(sqlQuery2, studs)

mydb.commit()

mydbCursor.execute("SELECT * FROM students")
for st in mydbCursor:
    print(st)

mydb.close() # close connection to DB