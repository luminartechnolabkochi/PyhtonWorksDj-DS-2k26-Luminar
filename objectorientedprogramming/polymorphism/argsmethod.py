



# define a class Calculator  with add method takes any number of parameter


class Calculator:

    def add(self,*args):

        print(sum(args))


calc_instance = Calculator()

calc_instance.add(100,200,300)


# *=> variable length argumanets as tuple

#** => dictionary

