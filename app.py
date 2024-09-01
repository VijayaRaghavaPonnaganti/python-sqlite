import sqlite3

#connect to SQLite Database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

#create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

#Insert a record 
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))

#Commit the changes
conn.commit()

#Query the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
  print(row)

#close the connection
conn.close()

