

from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="tripwisedb"
)

cursor = connection.cursor()

query="""

insert into user (name,email,password) values(%s,%s,%s)

"""

data=[
    ("abin","abiin@gmail.com","abinin@123"),
    ("cipin","cipin@gmail.com","cipin@123"),
    ("fipin","fipin@gmail.com","fipin@123"),
    ("gipin","gipin@gmail.com","gipin@123")
]

cursor.executemany(query,data)

connection.commit()
print("qurey executed......")

cursor.close()
connection.close()