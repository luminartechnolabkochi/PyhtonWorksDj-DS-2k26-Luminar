# w.a.p display  divisors of number num1

num1=int(input("enter number"))#8
num2=int(input("enter number"))#12

small_number = min(num1,num2)

for i in range(1,small_number+1):

    if num1%i==0 and num2%i==0:

        print(i)



