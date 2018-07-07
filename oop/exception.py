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

raise People('Can not create instance without settig person Surname', People, People.__name__)

# Utility of custom exceptions truly comes to light when creating a framework, library, or API that is intended for
# access by other programmers.
