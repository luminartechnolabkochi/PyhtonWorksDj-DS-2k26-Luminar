
def say_hi(n):

    if n==1:

        return
    
    print("hello",n)

    return say_hi(n-1)

say_hi(5)



def sum_of_n(n):

    if n==1:

        return 1
    
    return n+sum_of_n(n-1)

print(sum_of_n(3))



"""