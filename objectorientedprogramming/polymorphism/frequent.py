
# Polymorphism
    #method overloading
    #method overriding
# *args,**kwargs


class NumberCount:


    def solution(*args,**kwargs):

        num_list=list(args)

        val=kwargs.get("value") #10

        return num_list.count(val)


num_count_instance = NumberCount()

print(num_count_instance.solution(10,10,20,20,30,40,10,50,value=50))


