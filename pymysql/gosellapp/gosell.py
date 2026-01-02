
# create => class
# __init__
# CRUD method 
# try,except,finally,raise,assert

"""

	id int primary key auto_increment,
    name varchar(200) not null,
    price int not null,
    year varchar(200) not null,
    fuel_type enum('petrol','diesel','ev') default 'petrol',
    comments varchar(200),
    running_km int not null,
    owner_type enum('single','second','third','other') default 'single',
    created_at datetime default current_timestamp,
    status boolean default true,
    owner varchar(200) not null,
    location varchar(200) not null

"""

from mysql import connector


class Vehicles:

    def __init__(self):
        
        try:

            self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="gosell_db"
            )

            self.cursor = self.connection.cursor()

            print("db connection ok.....")
        
        except Exception as e:

            print(e)
   
    def add_vehicle(self,**kwargs):
        # kwargs={"name":"","price":,"year":,"fuel_type","comments":,"running_km"}

        try:

            columns=""
            values=""

            for k,v in kwargs.items():
                columns+=k+","
                values+="%s"+","

            columns= columns.rstrip(",")

            values=values.rstrip(",")

            query=f"""
            insert into vehicle ({columns}) values({values})
            """
        
            data=[v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record inserted")

        except Exception as e:

            print(e)

    def list_vehicles(self):

       try:
            query="select * from vehicle"

            self.cursor.execute(query)

            records=self.cursor.fetchall()

            for row in records:
                print(row)

       except Exception as e:
           
           print(e)

    def retrieve_vehicle(self,id=None):

        try:
            query="select * from vehicle where id = %s"

            data=(id,)

            self.cursor.execute(query,data)

            record=self.cursor.fetchone()

            print(record)
        
        except Exception as e:
            print(e)

    def delete_vehicle(self,id=None):

        try:

            query ="delete from vehicle where id = %s"

            data = (id,)
            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted  ....")

        except Exception as e:

            print(e)

    def update_vehicle(self,id,**kwargs):

        place_holder=""

        for k,v in kwargs.items():
            
            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update vehicle set {place_holder} where id={id} "

        data=[v for k,v in kwargs.items()]

        self.cursor.execute(query,data)
        self.connection.commit()

vehicle_instance = Vehicles()

# vehicle_instance.add_vehicle(name="passion pro",price=23000,year=2011,fuel_type="petrol",comments="good condition",running_km=12000,owner_type="single",owner="vijay",location="kakkanad")

# vehicle_instance.list_vehicles()

vehicle_instance.retrieve_vehicle(id=3)

vehicle_instance.update_vehicle(id=3,price=30000,year=2022)

vehicle_instance.retrieve_vehicle(id=3)
# vehicle_instance.delete_vehicle(id=2)

# vehicle_instance.list_vehicles()

print("all good ........")

