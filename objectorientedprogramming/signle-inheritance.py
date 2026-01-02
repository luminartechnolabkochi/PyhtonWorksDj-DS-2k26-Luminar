


class Person:

    name:str

    age:int

    gender:str

    def __init__(self,name,age,gender):

        self.name = name

        self.age = age

        self.gender = gender

    def display(self):

        print(f"Name={self.name} Age={self.age} Gender={self.gender}")


class Student(Person): #

    roll_number:str

    course:str

    def __init__(self, name, age, gender,rol,course):

        super().__init__(name,age,gender)

        self.rol = rol

        self.course = course

    def display(self):

        super().display()

        print(self.rol,self.course)

student_intsnce1=Student("hari",34,"male",1234,"django")

student_intsnce1.display()





        


