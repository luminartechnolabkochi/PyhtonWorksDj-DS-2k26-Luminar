

#  0 1 1 2 3 
#      p c n

# program to find factorial
class Factorial:

    def solution(self,number):

        fact = 1

        for i in range(1,number+1):

            fact *=i

        print(fact)


fact_instance = Factorial()

fact_instance.solution(5)