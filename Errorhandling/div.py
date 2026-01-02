

num1=int(input("enter number1"))

num2=int(input("enter number1"))

try:
    result = num1/num2

    print(result)

except Exception as e:

    num2=int(input("enter number"))#=>error stop

    result=num1/num2

    print(result)

finally:
    
    print("sending text message......")

    print("sending Email ......")

# try
# except
# finally
# raise
# assert