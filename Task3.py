# Implementing sqlite3 using Python.
import sqlite3

#connection to a database
con = sqlite3.connect("task3.db")

#creating a cursor
cur = con.cursor()

#Creating a table named employee
cur.execute('''CREATE TABLE employee (EmpID INTEGER PRIMARY KEY, GENDER, AGE, MaritalStatus, EXP, DEPT, EmpType)''')

#Inserting data into table
cur.execute('''INSERT INTO employee (EmpID, GENDER, AGE, MaritalStatus, EXP, DEPT, EmpType)
            VALUES (1,'M',35,'SINGLE',8,'COMPUTER SCIENCE','FULL-TIME')
            ,(2, 'F', 30,'MARRIED', 5,'DATA SCIENCE', 'PART-TIME')''')
con.commit()

# Adding data using executemany() method.
data = [
   (3,"M",28,"MARRIED",6,"DATA SCIENCE","FULL-TIME")
]
cur.executemany("INSERT INTO employee VALUES(?,?,?,?,?,?,?)", data)
con.commit()

#USING PARAMETERS
cur.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?)",(4,"M",40,"MARRIED",15,"INFORMATION SECURITY","FULL-TIME"))
con.commit()
#Printing of data in the table.
cur.execute("SELECT * FROM employee")
rows = cur.fetchall()
for row in rows:
    print(row)

#close cursor
cur.close()

#close connection
con.close()


