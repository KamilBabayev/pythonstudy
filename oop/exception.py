#!/usr/bin/python3

import os
tmp_data_dir = '/tmp'

# raise error example
if os.path.exists(tmp_data_dir) is True:
    print('Path {} exists'.format(tmp_data_dir))
elif os.path.exists(tmp_data_dir) is False:
    raise FileNotFoundError('Path does not exists')

# catch exception example
try:
    a= 30 / 0 
except ZeroDivisionError:
    print('Can not devide to Zero')

# Most exceptions are subclasses Exception class. Exception class itself actuallt inherits from a class 
# called BaseException. In fact, all exceptions must extend the BaseException class or one of its subclasses.
# There are two key exceptions, SystemExit and KeyboardInterrupt , that derive directly from BaseException 
# instead of Exception . The SystemExit exception is raised whenever the program exits naturally, 
# typically because we called the sys.exit function somewhere in our code
# The KeyboardInterrupt exception is common in command-line programs. It is thrown when the user explicitly
# interrupts program execution with an OS-dependent key combination (normally, Ctrl + C).

# Often, when we want to raise an exception, we find that none of the built-in exceptions are suitable.
# Defining our own exceptions:
class InvalidWithdrawal(Exception):
    pass

#raise InvalidWithdrawal('You do not have this amount in your account')

class People(Exception):
    pass

#raise People('Can not create instance without settig person Surname', People, People.__name__)

# Utility of custom exceptions truly comes to light when creating a framework, library, or API that is intended for
# access by other programmers.

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass
class PasswordTooShort(AuthException):
    pass

number = 33
if number != 30:
    raise Exception('Number is different than 30')

# Since Exceptions are objects and can be constructed, it makes sense that we can subclass the Exception class. Or even subclass subclasses of the Exception class.
class MyException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class MyIndexError(IndexError):
    def __init__(self,*args,**kwargs):
        IndexError.__init__(self,*args,**kwargs)

# It is better use default exceptions. if they do not include create your own one.
# In real life, however no program nor library should ever raise Exception directly: it's not specific enough to be helpful.
# Always inherit from (at least) Exception:.  Leverage what we saw earlier about BaseException.__str__: it uses the first argument 
# passed to BaseException.__init__ to be printed, so always call BaseException.__init__ with only one argument. When building a library, 
# define a base class inheriting from Excepion. It will make it easier for consumers to catch any exception from the library:

class ShoeError(Exception):
    """Basic exception for errors raised by shoes"""

class UntiedShoelace(ShoeError):
    """You could fall"""

class WrongFoot(ShoeError):
    """When you try to wear your left show on your right foot"""

# It then makes it easy to use except ShoeError when doing anything with that piece of code related to shoes.


# Here is example how we take original exception and wrap with our own custome defined one.
a = 3
b = 'test'

class MyError(Exception):
    def __init__(self, msg, original_exception):
        super(MyError, self).__init__(msg + (": %s" % original_exception))
        self.original_exception = original_exception


class MyListError(Exception):
    def __init__(self, msg):
        super(MyListError, self).__init__(msg)

#try:
#    c = a + b
#except TypeError as e:
#    raise MyError("Please never try to sum string and intereger")

try:
    c = a + [1,2,3]
except TypeError as e:
    raise MyListError("Please never try to sum string and list")



















