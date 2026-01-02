


num1=int(input("enter number1 "))

num2=int(input("enter number2 "))

operaton = input("enter operation u want to perform + for add - sub * multi / for div")


match operaton:

    case "+":


        print("addition result",num1+num2)

    case "-":

        print("sub result",num1-num2)

    case "*":

        print("multipli result",num1*num2)

    case "/":

        print("div result",num1/num2)

    case _:

        print("invalid")
