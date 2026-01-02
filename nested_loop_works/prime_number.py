
# pattern
# print
# range
# type
# input
# round
# functions 

number = int(input("enter number"))# (1,number)#9

is_prime = True


for i in range(2,number):# [2,3,4,5,6,7,8]
    #                                 i

    if number%i==0:#9%4==0

        is_prime=False

        break

print(is_prime)

