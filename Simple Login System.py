# Made by Jordan Leich
# Created on 10/17/19
# Last updated on 5/20/2020
# Version 4.0


# Imports
import time

# Variables
get_user = str()
new_user = str()
existing_user = str()
new_account = str()
new_email = str()
new_password = str()
name = str()
old_email = str()
old_password = str()
try_again = str()
x = float()
y = float()
result = float()


# Start
def beginning():
    print()
    print("Please keep in mind that this program is case sensitive with your name, email, and password!  ")
    print()
    time.sleep(1)
    existing_user = input("Are you an existing user?  ")
    print()
    time.sleep(1)
    if existing_user == "yes" or existing_user == "y":
        old()

    if existing_user == "no" or existing_user == "n":
        new()


# Old Account
def old():
    global new_account
    name = input("Please enter the name on your account:  ")
    print()
    time.sleep(1)
    if name != "Jordan":
        print("The info you provided doesn't currently exist on our records.  ")
        print()
        try_again = input("Would you like to try again?  ")
        print()
        if try_again == "yes" or try_again == "y" or try_again == "Yes":
            old()
        if try_again == "no" or try_again == "n" or try_again == "No":
            new_account = input("Would you like to create a new account?  ")
            print()
            if new_account == "yes" or new_account == "y" or new_account == "Yes":
                make_account()
            if new_account != "yes" or new_account == "y" or new_account == "Yes":
                end()
    old_email = input("Please enter your existing email:  ")
    print()
    time.sleep(1)
    if old_email != "jordanleich@gmail.com":
        print("The info you provided doesn't currently exist on our records.  ")
        print()
        try_again = input("Would you like to try again?  ")
        print()
        if try_again == "yes" or try_again == "y" or try_again == "Yes":
            old()
        if try_again == "no" or try_again == "n" or try_again == "No":
            new_account = input("Would you like to create a new account?  ")
            print()
            if new_account == "yes" or new_account == "y" or new_account == "Yes":
                make_account()
            if new_account != "yes" or new_account == "y" or new_account == "Yes":
                end()
    old_password = input("Please enter your existing password:  ")
    print()
    time.sleep(1)
    if old_password == "random12345":
        logged_in()

    else:
        print("The info you provided doesn't currently exist on our records.  ")
        print()
        try_again = input("Would you like to try again?  ")
        print()
        if try_again == "yes" or try_again == "y" or try_again == "Yes":
            old()
        if try_again == "no" or try_again == "n" or try_again == "No":
            new_account = input("Would you like to create a new account?  ")
            print()
        if new_account == "yes" or new_account == "y" or new_account == "Yes":
            make_account()
        if new_account != "yes" or new_account == "y" or new_account == "Yes":
            end()


# Want to make a new account?
def new():
    new_account = input("Since you are currently not an existing user, would you like to become a new user?  ")
    print()
    if new_account == "yes" or new_account == "y":
        make_account()

    if new_account == "no" or new_account == "n":
        end()


# Making the new account
def make_account():
    name = input("Enter your first name:  ")
    print()
    time.sleep(1)
    new_email = input("Please enter a valid email:  ")
    print()
    time.sleep(1)
    new_password = input("Please enter a password:  ")
    print()
    time.sleep(1)
    confirm_password = input("Please confirm your new password:  ")
    print()
    time.sleep(1)
    if confirm_password != new_password:
        print("Your new password could not be confirmed!  ")
        print()
        time.sleep(1)
        print("You will now be prompted to another new account.  ")
        print()
        time.sleep(1)
        make_account()
    logged_in()


# Logging in
def logged_in():
    print("Logging in...")
    print()
    time.sleep(2)
    print("Congrats, you are currently logged in.  ")
    print()
    time.sleep(3)
    actions()


# Actions to take while the user is logged in
def actions():
    first_action = input("Would you like to use our simple math calculator (1) or Quit this program (2):    ")
    print()
    time.sleep(2)
    if first_action == "1":
        calc()

    elif first_action == '2':
        end()

    else:
        print("Invalid input!")
        print()
        time.sleep(2)
        print("restarting input...")
        print()
        time.sleep(1)
        actions()


# Simple calculator that a logged in user can use
def calc():
    print("Select an operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print()
    choice = input("Enter choice(1/2/3/4):  ")
    print()
    if choice == '1' or choice == 'add':
        add(x, y)

    elif choice == '2' or choice == 'subtract':
        subtract(x, y)

    elif choice == '3' or choice == 'multiply':
        multiply(x, y)

    elif choice == '4' or choice == 'divide':
        divide(x, y)

    else:
        print("Invalid input!")
        print()
        time.sleep(2)
        print("restarting calculator choice...")
        print()
        time.sleep(2)
        calc()


def add(x, y):
    num1 = input('Enter first number: ')
    print()
    num2 = input('Enter second number: ')
    print()
    sum = float(num1) + float(num2)
    print(sum)
    print()
    moremath()


def subtract(x, y):
    num1 = input('Enter first number: ')
    print()
    num2 = input('Enter second number: ')
    print()
    remainder = float(num1) - float(num2)
    print(remainder)
    print()
    moremath()


def multiply(x, y):
    num1 = input('Enter first number: ')
    print()
    num2 = input('Enter second number: ')
    print()
    product = float(num1) * float(num2)
    print(product)
    print()
    moremath()


def divide(x, y):
    num1 = input('Enter first number: ')
    print()
    num2 = input('Enter second number: ')
    print()
    quotient = float(num1) / float(num2)
    print(quotient)
    print()
    moremath()


def moremath():
    more_math = input("Would you like to do a another math problem(1) or quit this program(2):  ")
    print()
    time.sleep(2)
    if more_math == '1':
        calc()

    elif more_math == '2':
        end()

    else:
        print('Invalid input!')
        print()
        time.sleep(2)
        print('restarting choice...')
        print()
        moremath()


# Ending
def end():
    print("This is the end of the program - Jordan Leich")
    quit()


# Main Engine
beginning()
