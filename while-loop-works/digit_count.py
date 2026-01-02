

number  =int(input("enter number "))#123

count = 0#

while(number!=0):#123!=0 12!=0 1!=0 0!=0

    digit = number%10#digit=123%10=>3  12%10=2 1%10=1

    count = count+1#count=3

    number=number//10#12 12//10=1 1//10=0

print("no of digit",count)


