


class Employee:

    eid:int

    name:str

    salary:int

    dept:str

    def __init__(self,eid,name,salary,dept):

        self.eid = eid

        self.name = name

        self.salary = salary

        self.dept = dept

    def display(self):

        print("employee id=",self.eid) 
        print("employee name=",self.name) 
        print("employee salary=",self.salary)


emp_instance1=Employee() 

emp_instance2=Employee()

emp_instance2.set_employee(123,"hari",34000,"hr")

emp_instance1.set_employee(345,"vipin",45000,"qa")

emp_instance2.display()

emp_instance1.display()



# constructor is a normal method
# special name __init__()
# initialize instance variables
# automatically invoked during object creation
