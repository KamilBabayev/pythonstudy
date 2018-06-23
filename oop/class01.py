#!/usr/bin/python3

class Contact():
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print(order, self.name)

c = Contact('Kamil', 'kamil@demo.local')
s = Supplier('John', 'john@demo.local')

print(c.name, c.email, s.name, s.email)
print(s.order('Salam'))                 # as yuo see order must print self.name and it inherits this from paret class

# Now ex. I will new class, which must have phone attr beside name and email, here either i can add this to Contact class(which will
# cause many changes in subclasses ) or I will create new __init__ in new class and override Contact.This is called overriding.
# This is in case , when we must inherit from Contact class for any reason. Subclass can override any parent method. Ex:

class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name  = name
        self.email = email
        self.phone = phone

# But here is one problem, there are many duplicate code in Friend class, which were in Contact also.
# It is better to execute __init__ method from Contact without overriding.super() - comes to help here - it
# returns the object as an instance of the parent class, allowing us to call parent class directly.

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# This example first gets the instance of the parent object using super, and calls __init__ on that object, passing
# the expected arguments. It then does its own initialization, namely, setting the phone attribute.
# A super() call can be made inside any method , not just __init__.

# Mutiple inheritance - it is recommended to aviod this. when needed try to implement via other ways. Ex:
class Friend(Contact, Supplier):
    pass

class Friend(Demo1, Demo2):
    def __init__(self, name, email, phone, address):
        Demo1.__init__(self, name, email)
        Demo2.__init__(self, phone)
        self.address = address

# Here we inherit from 2 classes. after main __init__ we call each parent instructor by sequence.
# problems are, if we forget to initialize one of parents, it could cause problems later. second every parent has
# object parent, which is called  once (in general twice) here by each of them.

