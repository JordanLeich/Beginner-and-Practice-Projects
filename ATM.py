# Made by Jordan Leich on 5/23/2020

# Imports
import math
import time


def start():
    print()
    print('Welcome to the banking ATM app, this program allows you to use a bank atm with a deposit and withdrawal '
          'option.')
    print()
    time.sleep(1)
    choice()


def choice():
    choice1 = str(input("Would you like to deposit(1), withdrawal(2), or quit(3): "))
    print()
    time.sleep(2)

    if choice1 == '1':
        deposit()

    elif choice1 == '2':
        withdrawal()

    elif choice1 == '3':
        print("Exiting program...")
        time.sleep(2)
        quit()

    else:
        print("Invalid input, ending program...")
        print()
        time.sleep(2)
        quit()


def deposit():
    updated_balance = int
    balance = int(input('Enter your balance: '))
    print()

    if balance < 0:
        print("Your balance is negative! Deposit soon to avoid any unwanted overdraft fees! ")
        print()
        deposit_amount = int(input('Deposit amount: '))
        print()
        print("Your new balance is: ", balance + deposit_amount)
        print()
        if balance + deposit_amount < 0:
            print("Your balance is still negative! Deposit more as soon as possible and avoid withdrawing until your "
                  "balance becomes positive to avoid overdraft fees!")
            print()
            time.sleep(2)
            choice()

        elif balance + deposit_amount > 0:
            deposit_amount = int(input('Deposit amount: '))
            print()
            print("Your new balance is: ", balance + deposit_amount)
            print()
            time.sleep(2)
            choice()

        else:
            print('Error caught! ending program...')
            print()
            time.sleep(2)
            quit()

    elif balance > 0:
        deposit_amount = int(input('Deposit amount: '))
        print()
        print("Your new balance is: ", balance + deposit_amount)
        print()
        time.sleep(2)
        choice()

    else:
        print("Invalid input, ending program...")
        print()
        time.sleep(2)
        quit()


def withdrawal():
    balance = int(input('Enter your balance: '))
    print()

    if balance < 0:
        overdraft_choice = str(input(
            "Your balance is negative! if you wish to continue, you will face an overdraft of 36 dollars(yes or no): "))
        print()
        if overdraft_choice == 'yes' or overdraft_choice == 'y':
            deposit_amount = int(input('Withdrawal amount: '))
            print()
            print("Your new balance is: ", (balance - deposit_amount) - 36)
            print()
            if (balance - deposit_amount) - 36 < 0:
                print(
                    "Warning! your updated balance is still negative, try avoiding withdrawing anymore until your "
                    "balance "
                    "is positive again to avoid any overdraft fees!")
                print()
                time.sleep(2)
                choice()

            elif (balance - deposit_amount) - 36 > 0:
                time.sleep(2)
                choice()

            else:
                print('Error caught! ending program...')
                print()
                time.sleep(2)
                quit()

        elif overdraft_choice == 'no' or overdraft_choice == 'n':
            negative_choice = input("Since your balance is negative and you didnt want to withdrawal, would you like "
                                    "to either deposit(1) or quit this program(2): ")
            print()
            time.sleep(2)
            if negative_choice == '1':
                deposit()

            elif negative_choice == '2':
                print("ending program...")
                print()
                time.sleep(2)
                quit()

            else:
                print("Invalid input, ending program...")
                print()
                time.sleep(2)
                quit()


        else:
            print("Invalid input, ending program...")
            print()
            time.sleep(2)
            quit()


    elif balance > 0:
        deposit_amount = int(input('Withdrawal amount: '))
        print()
        print("Your new balance is: ", balance - deposit_amount)
        print()
        if balance - deposit_amount < 0:
            print("Warning! your updated balance is now negative, try avoiding withdrawing anymore until your balance "
                  "is positive again to avoid any overdraft fees!")
            print()
            time.sleep(2)
            choice()

        elif balance - deposit_amount > 0:
            time.sleep(2)
            choice()

        else:
            print("Error caught! ending program...")
            print()
            quit()

    else:
        print("Invalid input, ending program...")
        print()
        time.sleep(2)
        quit()


start()
