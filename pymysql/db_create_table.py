from mysql import connector

connection=connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="work_log_db"
)

cursor=connection.cursor()



query = """
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
"""

cursor.execute(query)


cursor.close()
connection.close()

