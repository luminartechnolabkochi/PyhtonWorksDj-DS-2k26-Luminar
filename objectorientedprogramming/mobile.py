

class Mobile:

    title:str

    brand:str

    price:int


    def __init__(self,title,brand,price):

        self.title = title

        self.brand=brand

        self.price = price

    def display(self):

        print(f"Title:{self.title} Brand{self.brand} Price{self.price}")


mob_instance1=Mobile("redmi note 15 pro","redmi",24000)

mob_instance1.display()



"""
# oop features
# inheritance
=============
    mechanisam of child class accessing parent class attributes and methods 
    1)single inheritance
    2)multilevel inheritance
    3)multiple inheritance 

# polymorphism 

    many forms (more than one form)

    1)method overloading
    
    2)method overriding


# abstraction

    hiding implimentation details


"""

