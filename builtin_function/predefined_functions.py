"""
print("message")->None : [display message in console]

input("message")->str   :read value through console

type(object)-> int|float|bool|str|list|tuple|set|dict: return data type of object

sum(*args)->int : return sum of arguments

max(*args)->int :return highest value

min(*args)->int :return smallest number

*len(object)=>int : return length of object

sorted(*args,reversed=False):->return sorted args

*round(number,ndigits)=> round number

*range(start,stop,step)->sequence of numbers from start to end

absolute(number)-> return absolute value of number

enumerate(list|string,start=0)=>return value and index

open(file_path,mode)-> for creating file references

dir(class) -> return all methods present inside class 
=====================================================
map()

filter()

reduce()

any()

all()


"""




lst=[100,200,300,400]
#     0    1   2   3

for index,num in enumerate(lst):

    print(index,num)
