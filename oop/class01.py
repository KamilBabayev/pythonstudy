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
