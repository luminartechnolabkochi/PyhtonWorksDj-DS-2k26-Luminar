



class Animal:

    def __init__(self,name):

        self.name = name

    

    def sound(self):

        print(self.name,"sound")



class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):

        print(self.name ,"bark")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        
        print(self.name,"meow")

    

dog_instance = Dog("Dog")

dog_instance.sound()


cat_instance = Cat("cat")

cat_instance.sound()

# method overloading
    # same method name different number of parameters

# method overriding

    #child class changes the behaviur of method that it gets from parent class 


# function -> variable length argument method
#   

