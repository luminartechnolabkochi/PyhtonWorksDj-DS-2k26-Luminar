

number = int(input("enter number "))#28

result = 0

for i in range(1,number):

    if number%i==0:

        result+=i


if number == result :

    print("perfect number")

else:
    print("not a perfect number")

