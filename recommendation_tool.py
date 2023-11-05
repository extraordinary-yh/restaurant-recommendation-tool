#!/usr/bin/env python
# coding: utf-8


# The code here will ask the user for input based on the askables. It will only ask the user where necessary.
# Inspired by code from R.Shekhar

# Import necessary packages
import tempfile
from pyswip.prolog import Prolog
from pyswip.easy import *
import string

prolog = Prolog() # Global handle to interpreter

retractall = Functor("retractall")
known = Functor("known",3)

print("**Welcome to Choose Your Dream Restaurant**")
print("We will be asking a set of questions to narrow down on what restaurant you should go to")
# Define foreign functions for getting user input and writing to the screen
def write_py(X):
    for index, val in enumerate(X):
        print(index+1 , str(val))
    sys.stdout.flush()
    return True

def read_py(A, Ans, Menu):
        if str(A) == 'cuisine':
            if isinstance(Ans, Variable):
                print("Which cuisine you want to go with today?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'diet':
            if isinstance(Ans, Variable):
                print("What is your go to diet?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'activity':
            if isinstance(Ans, Variable):
                print("Do you want there to be any activty at the restaurant?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'distance':
            if isinstance(Ans, Variable):
                print("How far are you willing to go for food?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v).replace("_", " "))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'number_of_people':
            if isinstance(Ans, Variable):
                print("How many people are going?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v).replace('_', ' '))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'budget':
            if isinstance(Ans, Variable):
                print("How financially stable are you?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v).replace('_', ' '))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'atmosphere':
            if isinstance(Ans, Variable):
                print("Do you want eat in peace or do you want to go to a rowdy place?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v).replace('_', ' '))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False
        if str(A) == 'outdoor_sitting':
            if isinstance(Ans, Variable):
                print("Are you looking to sit outside and enjoy the beautiful weather?")
                for i, v in enumerate(Menu):
                    print(i+1, str(v))
                response = input()
                while not response.isdigit() or int(response) > len(Menu) or int(response) <= 0:
                    print("Wrong input. Please try inputting a valid integer.")
                    response = input()
                response = int(response)
                Ans.unify(str(Menu[response-1]))
                return True
            else:
                return False

write_py.arity = 1
read_py.arity = 3

registerForeign(read_py)
registerForeign(write_py)

# Create a temporary file with the KB in it
(FD, name) = tempfile.mkstemp(suffix='.pl', text = "True")
with os.fdopen(FD, "w") as text_file:
    text_file.write(KB)
prolog.consult(name) # open the KB for consulting
os.unlink(name) # Remove the temporary file

call(retractall(known))
restaurant = [s for s in prolog.query("restaurant(X).", maxresult=1)]
if restaurant:
    print("You should probably go to " + string.capwords(str(restaurant[0]['X']).replace('_', ' ')) + ".")
else:
    print("Your on your own chief.")




