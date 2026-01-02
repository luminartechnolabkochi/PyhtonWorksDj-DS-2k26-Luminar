"""
Abstraction
hiding implimentaion details 

"""


# ATM-> select transaction type -> Verify pin -> withdraw -> cash collect



# Car [start,stop,accelerate]

from abc import ABC
from abc import abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Swift(Car):

    def start(self):
        print("swift car starting")

swift_instance = Swift()

swift_instance.start()





# inheritance
    #single
    # multilevel
    # multiple
# polymorphism
    #more than one form
    # method overloading : *args, **kwargs
    # method overriding
# abstraction
    #hiding implimentatiion detail
    # abc.py => class ABC, abstract_method


