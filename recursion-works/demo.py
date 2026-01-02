"""
recursion
 :a function call itself is called recusrion

"""


def display_hello_world(limit):

    if limit==0:

        return 
    
    print("Hello World")

    return display_hello_world(limit-1)


display_hello_world(5)




def display_numbers(limit):

    if limit==0:
        return 
    
    print(limit)

    return display_numbers(limit-1)

# display_numbers(10)

# 15
# 15,,,,1



# sum of n numbers using recusrion



def sum_of_n(limit):

    if limit==1:

        return 1
    
    return limit+sum_of_n(limit-1)

print(sum_of_n(5))

"""
sum_of_n(5)
5+sum_of(4)=>5+10=>15
4+sum_of(3)=>4+6=>10
3+sum_of(2)=>3+3=>6
2+sum_of(1)=>2+1=>3
sum_of(1)=>1
"""




def factorial(number):

    if number==0:
        return 1
    
    return number*factorial(number-1)

# print(factorial(5))


# sum_of_digit(number)
# sum_of_digit(543) => 12 recursion



def sum_of_digit(number):

    if number==0:
        return 0
    
    return number%10+sum_of_digit(number//10)

# print(sum_of_digit(234))


# product_of_digit(number)


def product_of_digit(number):

    if number==0:

        return 1
    
    return number%10*product_of_digit(number//10)

# print(product_of_digit(123))


# reverse_number(num)


def reverse_int(number):

    if number==0:

        return ""
    
    return str(number%10)+ str(reverse_int(number//10))

print(reverse_int(234))

# database


name="sabir"

course="datascience"

# file
# database Mysql

# database => sql queries 

# Mysql (install= database[data store])



# recursion

# def funciont_name(p):

    # base condition

    # return function_name(p)


