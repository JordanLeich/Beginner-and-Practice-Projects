# Made by Jordan Leich
# Created on 10/17/19
# Version 2.8


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


# Start
def beginning():
    print("Please keep in mind that this program is case sensitive with your name, email, and password!  ")
    print()
    time.sleep(1)
    existing_user = input("Are you an existing user?  ")
    print()
    if existing_user == "yes" or existing_user == "y":
        old()

    if existing_user == "no" or existing_user == "n":
        new()


# Old Account
def old():
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
    if old_password != "Jordan1":
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
    logged_in()


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
    print("Please wait...logging in...")
    print()
    time.sleep(2)
    print("Congrats, you are currently logged in.  ")
    print()
    time.sleep(3)
    end()


# Ending
def end():
    print("This is the end of the program - Jordan Leich")
    quit()


# Main Engine
beginning()
