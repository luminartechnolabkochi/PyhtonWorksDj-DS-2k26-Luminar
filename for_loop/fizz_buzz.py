# w.a.p to display numbers from 1 to 100
# while displaying 
    # if num is / by 3 print fizz
    #  if num is / by 5 print BUZZ
    #  if num is / by 15 print FIZZBUZZ
    # else display number

# 1 ,2,fizz,4,buzz,fizz,

for num in range(1,101):

    if num%15==0:

        print("FIZZBUZZ")

    elif num%5==0:

        print("BUZZ")

    elif num%3==0:

        print("FIZZ")

    else:
        print(num)