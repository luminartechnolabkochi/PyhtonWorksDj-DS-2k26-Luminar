"""
Errorhandling
=============
    1.sytax error 
    2.logical error 
    3.runtime error (exception)

    block and keywords

    try:
        doubtful code

    except:
        handling code
    
    finally:
    
        cleanup process

"""

# Exception

# ZeroDivisionError  FileNotFound  KeyError ValueError

num1 = int(input("enter number1"))#10

num2 = int(input("enter number1"))#0


try:
    result = num1 / num2#10/0 => error ZeroDivisionError

    print(result)#5.0

except Exception as e:
    print(e)

print("file operation")

print("database commit")