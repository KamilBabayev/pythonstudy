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

