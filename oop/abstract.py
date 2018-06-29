#!/usr/bin/python3

# By defining an abstract base class, you can define a common API for a set of subclasses.
# Abstract classes is a way to force a subclass to implement methods. Abstract classes can contain abstract methods: 
# methods without an implementation. Objects cannot be created from an abstract class. A subclass can implement an abstract class.
# Ex: we can create base class from(like creating baseline which contains method definition, not implementation.) this base class
# we create subclasses. And this subclasses must have implementation of defined methods which has been defined in base class.)
# Ex we have truck and sedan car. both must have start and stop method. we create Automobile base class and and define abstract methods in it. 
# both sedan and truck classes inherit this Automobile abstract class and must implement abstacrt start and stop methods. if not will throw out 
# NotImplementedError exception. We urge subclass user to implment methods as we required.

from abc import ABC, ABCMeta, abstractmethod

class Automobile(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


'''
class Truck(Automobile):
    "data"

car01 = Truck()
'''
# here I get below error. because I have not implemented required start and stop methods.
# TypeError: Can't instantiate abstract class Truck with abstract methods start, stop

'''
class Truck(Automobile):
    def start():
        print("sdsd")

a = Truck()

Now I get this error. Because i have implmented start only. I must so stop also. this is demanded from baseclass as we explained above.
TypeError: Can't instantiate abstract class Truck with abstract methods stop
'''

class Sedan(Automobile):
    def start(self):
        print("starting")
    def stop(self):
        print('stopping..')

car02 = Sedan()

'''
Now I do not get any error because I have implemented both methods start and stop.
'''



