import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
connect2 = sqlite3.connect('new.db')

# Create a cursor object using the cursor() method
cursor = connect2.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS stk1
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cursor.execute("INSERT INTO stk1 VALUES ('2024-01-05','SEL', 'A', 88, 25.12)")

# Save (commit) the changes
connect2.commit()

cursor.execute("SELECT * FROM stk1")
rows = cursor.fetchall()

for row in rows:
  print(row)

# Close the connection
connect2.close()

