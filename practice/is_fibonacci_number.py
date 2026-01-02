
# 8
# 0 1 1 2 3 5 8 13 21

# write a program to chk given number is a fibonacci number or not


class IsFibonacciNumber:

    def solution(self,number):

        is_fibo_number = False        
        p=0
        c=1
        n=p+c
        while(n<=number):

            n=p+c
            p=c
            c=n
            if n==number:
                is_fibo_number=True
            

      
        return is_fibo_number

is_fibo_instance=IsFibonacciNumber()

print(is_fibo_instance.solution(14))
