# step1 => install mysql
#pip install mysql-connector-python



from mysql import connector

# create db connection

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="work_log_db"

)

print("connection success")

# creating cursor object for executing queries

cursor = connection.cursor()

# creating table 

query = """
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
"""

cursor.execute(query)
connection.commit()

# Insert Data
query = "INSERT INTO student (name, age) VALUES (%s, %s)"
data = ("Rahul", 22)

cursor.execute(query, data)
connection.commit()

print("Data inserted")


# Fetch Data (SELECT)
cursor.execute("SELECT * FROM student")

result = cursor.fetchall()

for row in result:
    print(row)


# Update Data
query = "UPDATE student SET age = %s WHERE name = %s"
cursor.execute(query, (25, "Rahul"))
connection.commit()

# Delete Data
query = "DELETE FROM student WHERE name = %s"
cursor.execute(query, ("Neha",))
connection.commit()

# Close Connection (Imcursor.close()
cursor.close()
connection.close()

