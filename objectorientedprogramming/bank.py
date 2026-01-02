"""
Objected Oriented Programming

class => design , plan,template for creating object
object=>real world entity

class ClassName:

    attributes
    methods

"""



class Bank:

    acc_num:str

    name:str

    acc_type:str

    balance:int


    def create_account(self,acc_num,name,acc_type,balance):

        self.acc_num=acc_num

        self.acc_type=acc_type

        self.name = name
        self.balance = balance

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account{self.acc_num} credited with {amount} your avl bal is{self.balance}")

    def withdraw(self,amount):

        if amount<self.balance:

            self.balance-=amount
            
            print(f"your account{self.acc_num} credited with {amount} your avl bal is{self.balance}")

        else:

            print("trasaction failed insufficient balance")

    def balance_enq(self):

        print(f"hai {self.name} your acc bal is {self.balance}")



bank_acc_instance1=Bank()

bank_acc_instance1.create_account(1234,"jhon","savings",5000)

bank_acc_instance1.deposit(10000)

bank_acc_instance1.withdraw(10000)





    
# initialize attributes
# instance variables initialize => constructor




