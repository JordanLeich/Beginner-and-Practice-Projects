# Program information =================================================================================================|
# Program created by: Jordan Leich                                                                                     |
# Program created on: 9/4/19                                                                                           |
# Program version 2.3                                                                                                  |
# =====================================================================================================================|

# Imports
import time
import math

# Variables
pi = 3.14
Pi = 3.14

# Asking the user for their name
try:
    name = input("What is your name? ")
    print()
except ValueError:
    print("Invalid Name!")


# Entire operation
def user_input():
    global result
    print()
    print("Keep in mind that you can use Pi or 3.14 with this calculator!  ")
    print()
    time.sleep(2)
    number1 = float(input("What is your first number: "))
    print()
    number2 = float(input("What is your second number: "))
    print()
    try:
        operator1 = input(
            "Choose and type either 'add' 'subtract' 'multiply' 'divide' 'mod' 'remainder division' or '+' "
            "'-' '*' '**' '/' '//' ")
    except NameError:
        print("Invalid Operator!")

    print()

    if operator1 == "+" or operator1 == "add":
        result = (number1 + number2)

    if operator1 == "-" or operator1 == "subtract":
        result = (number1 - number2)

    if operator1 == "*" or operator1 == "multiply" or operator1 == "times":
        result = (number1 * number2)

    if operator1 == "**":
        result = (number1 ** number2)

    if operator1 == "/" or operator1 == "divide" or operator1 == "division":
        result = float(number1 / number2)

    if number1 == 0 or number2 == 0 and operator1 == "/" or operator1 == "divide" or operator1 == "division":
        print(ZeroDivisionError)
        print("You cannot divide by zero!")

    if operator1 == "//":
        result = (number1 // number2)

    if operator1 == "mod" or operator1 == "remainder division":
        print("In order to do this operation, your first number must to be bigger than your second number.")
        print()
        time.sleep(2)
        print("You also want to make sure that the division between your numbers will leave a remainder.")
        print()
        time.sleep(2)
        result = (number2 % number1)

    print("Your name is " + name + " and your final answer equals " + str(result))
    print()
    time.sleep(3)


# Start over
def start_over():
    print()
    operator2 = input("Do you want to solve another math problem? Answer with either yes or no: ")
    try:
        if operator2 == "yes" or operator2 == "sure" or operator2 == "y" or operator2 == "yeah":
            user_input()
            start_over()

        if operator2 == "no" or operator2 == "nope" or operator2 == "n" or operator2 == "nah":
            end()
    except ValueError:
        print("Invalid Choice!")
        end()


# End
def end():
    time.sleep(1)
    print()
    print("You are done solving math problems, thanks for using this program - Jordan Leich")


# Main Engine
user_input()
start_over()
