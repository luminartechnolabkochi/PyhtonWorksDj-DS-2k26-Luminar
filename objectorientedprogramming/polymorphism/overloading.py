"""
MethodOverloading:
    same method name different number of parameters with in a class

"""

class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    
    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    
    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)


cal_instance=Calculator()
cal_instance.add(100,200)#error num3,num4 missing
cal_instance.add(100,200,300,400)#1000
