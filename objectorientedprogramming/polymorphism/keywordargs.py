
# **kwargs
# *args

def display_person(**kwargs):
    #args=("hari",23,"tvm","kakkanad",34500)

    print(kwargs)


display_person(name="hari",age=23,n_place="tvm",w_place="kakkanad",salary=34500)





def operation(*args,**kwargs):
    #args(10,20,30,40)
    #kwargs={"key":"max"}

    op=kwargs.get("key")#max,min

    if op=="max":

        return max(args)
    else:
        return min(args)

print(operation(10,20,30,40,key="max"))

print(operation(10,20,30,40,key="min"))

