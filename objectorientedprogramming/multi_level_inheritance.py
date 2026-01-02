

class GrandParent:

    def properties(self):

        print("50cent land 1 huge vintage home")

class Parent(GrandParent):

    def vehicle(self):

        print("swift car")


class Child(Parent):

    def gadgets(self):

        print("iphone, ipad laptop")

child_instance = Child()

child_instance.gadgets()

child_instance.vehicle()

child_instance.properties()
