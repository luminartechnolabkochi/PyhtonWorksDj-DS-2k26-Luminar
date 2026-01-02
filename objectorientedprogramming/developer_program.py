

class Employee:

    id:int

    department:str

    salary:int

    def __init__(self,id,department,salary):

        self.id = id

        self.department = department

        self.salary = salary

    def display(self):

        print(f"id={self.id} Dept={self.department} salary={self.salary}")


class Developer(Employee):


    programming_language:str

    frame_work:str

    def __init__(self, id, department, salary,programming_language,frame_work):

        super().__init__(id,department,salary)

        self.programming_language=programming_language

        self.frame_work = frame_work

    def display(self):

        super().display()

        print(self.programming_language,self.frame_work)




developer_instance = Developer(123,"hr",35000,"python","django")

developer_instance.display()


