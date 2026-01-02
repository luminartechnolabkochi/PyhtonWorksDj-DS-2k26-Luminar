"""
defnition : set of reusable code used to perform a specific task

syntax

    1_function defnition
    2_function calling


    def function_name(p1,p2,p3,,,,pn):
        
        function body

    function_name(arg1,arg2)

"""



# creat a function greetings that display good morning


# create a function max_two with two parameter n1,n2 should return largest number

# create a function min_two with two param n1,n2 return smallest number

def min_two(n1,n2):


    return n1 if n1<n2 else n2





def max_two(n1,n2):

    return n1 if n1>n2 else n2

print(max_two(100,200))

print(min_two(100,20))



# create a function is_odd with one param n return True if number is odd else return False
def is_odd(n):

    return True if n%2!=0 else False

print(is_odd(10))



# create a function last_digit_max of two number



def last_digit_max(n1,n2):

    return n1 if n1%10 > n2%10 else n2

print(last_digit_max(278,871))


# create a function is_leap_year with one param year retur True 
# if year is leap year else return False

def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    
    else:

        return False
    
print(is_leap_year(2024))
print(is_leap_year(2025))
print(is_leap_year(2026))




# create function bmi with two parameter height_in_cm and weight_in_kg
# return bmi 



def bmi(height_in_cm,weight_in_kg):

    height_in_meter= height_in_cm/100

    result = weight_in_kg/(height_in_meter**2)

    return round(result,2)

print(bmi(165,75))



# q1
# create a function emi with parameter s
# amount(loan amount)
# tenure(in years)
# rate(interest rate)
# return monthly emi

# q2
# create a function factorial with one parameter number 
# return factorial of number

# q3
# creata function common_divisor with one parameter number
# return common divisors of number

# q4
# create a function gcd with two parameter num1,num2
# return gcd of two numbers

# q5
# create a function is_prime with one parameter
# return True if number is primenumber else return False


def factorial(number):

    result = 1

    for i in range(1,number+1):

        result = result*i

    return result

# print(factorial(5))



def divisors(number):

    for i in range(1,number+1):

        if number%i==0:

            print(i)

# divisors(6)


def gcd(num1,num2):

    smallest_number = min(num1,num2)

    result = 1

    for i in range(1,smallest_number+1):

        if num1%i==0 and num2%i==0:

            result = i
    return result 


print(gcd(12,24))

def is_perfect_number(number):

    sum = 0

    for i in range(1,number):

        if number%i==0:

            sum+=i
    
    return sum == number

print(is_perfect_number(28))





def is_prime(number):

    flag=True

    for i in range(2,number):

        if number%i==0:

            flag = False

            break 

    return flag


print(is_prime(7))

print(is_prime(11))

print(is_prime(9))



# string

