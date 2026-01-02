

from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor=connection.cursor()

query = "update user set name=%s,password=%s where id =%s "

data=("vipindas","vipindas@123",2)
cursor.execute(query,data)

connection.commit()

cursor.close()
connection.close()
