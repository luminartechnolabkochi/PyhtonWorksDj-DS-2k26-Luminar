"""
Docstring for objectorientedprogramming.inheritance
inheritance

mechanisam of child class accesing properties and attributes of parent class

syntax:

class Parent:

    def m1(self):
        print("parent class m1 method")

        
class Child(Parent):

    def m2(self):
    
        print("child class m2 method")


child_instance =Child() 

child_instance.m2()

child_instance.m1()


"""

class Parent:

    def vehicle(self):

        print("passion pro")

class Child(Parent):

    def mobile(self):

        print("oppo reno40")

child_instance = Child()

child_instance.mobile()

child_instance.vehicle()
