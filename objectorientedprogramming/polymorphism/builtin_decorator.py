



# create a class person with attributes name,age,gender and initialize 
# these attributes while creating object


class Person:

    def __init__(self,name,age,gender):

        self.name =  name

        self.gender = gender

        self.age = age

    @property
    def get_age(self):

        print(self.age)

    @property
    def get_gender(self):

        print(self.gender)


person_instance1 = Person("sai",23,"male")

person_instance1.get_age
    
person_instance1.get_gender

