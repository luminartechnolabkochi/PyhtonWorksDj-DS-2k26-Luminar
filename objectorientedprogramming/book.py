

class Book:

    title:str

    author:str

    price:str

    pages:int


    def __init__(self,title,author,price,pages):

        self.title = title

        self.author = author

        self.price = price
        
        self.pages = pages

    def display(self):

        print(f"book title:{self.title} author:{self.author} price:{self.price}")


book_instance1=Book("randamoozham","mt",456,556)

book_instance1.display()

print(type(book_instance1))
# constructor
# normal method
# special name class name  python[__init__]
# automatically invoked during object creation

# Mobile
# title,price,brand,features

