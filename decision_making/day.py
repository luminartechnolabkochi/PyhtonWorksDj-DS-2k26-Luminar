

# prompt a user to enter a day between 1 to 7
# 1 -5 display weekday
# 6-7 display weekend
# print()
# input()
# round(num,ndigit)
# range(start,stop)

day =int( input("enter a day 1-7"))#-2


if day in range(1,6):

    print("weekday")

elif  day in range(6,8):

    print("weekend")

else:

    print("invalid")

