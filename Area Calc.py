# Made by Jordan Leich
# Created on 10/19/19
# Version 2.4

# Imports


def start():  # Beginning of program
    ask_user = str(input("Do you want to find the area of a circle, square, rectangle, trapezoid, or triangle:  "))
    print()

    if ask_user == "circle" or ask_user == "Circle" or ask_user == "c" or ask_user == "C":
        circle()

    if ask_user == "square" or ask_user == "Square" or ask_user == "s" or ask_user == "S":
        square()

    if ask_user == "triangle" or ask_user == "Triangle" or ask_user == "t" or ask_user == "T":
        triangle()

    if ask_user == "rectangle" or ask_user == "Rectangle" or ask_user == "r" or ask_user == "R":
        rectangle()

    if ask_user == "trapezoid" or ask_user == "Trapezoid" or ask_user == "trap" or ask_user == "Trap":
        trapezoid()

    else:
        print("Invalid Input!  ")
        print()
        quit()


def trapezoid():  # Trapezoid
    base1 = float(input("What is the first base of your trapezoid:  "))
    print()
    base2 = float(input("What is the second base of your trapezoid:  "))
    print()
    height = float(input("What is the height of your trapezoid:  "))
    print()
    area_trapezoid = ((base1 + base2) / 2) * height
    print("The area of your circle is " + str(area_trapezoid))
    print()
    try_again = input("Do you wish to solve another area problem:  ")
    print()
    if try_again == "yes" or try_again == "Yes" or try_again == "y":
        start()
    else:
        end()


def circle():  # Circle
    radius = float(input("What is the radius of your circle:  "))
    area_circle = (3.14 * radius * radius)
    print()
    print("The area of your circle is " + str(area_circle))
    print()
    try_again = input("Do you wish to solve another area problem:  ")
    print()
    if try_again == "yes" or try_again == "Yes" or try_again == "y":
        start()
    else:
        end()


def rectangle():  # Rectangle
    length = float(input("What is the length of your rectangle:  "))
    print()
    width = float(input("What is the width of your rectangle:  "))
    print()
    area_rectangle = (length * width)
    print()
    print("The area of your rectangle is " + str(area_rectangle))
    print()
    try_again = input("Do you wish to solve another area problem:  ")
    print()
    if try_again == "yes" or try_again == "Yes" or try_again == "y":
        start()
    else:
        end()


def square():  # Square
    side = float(input("What is the length of one side of your square:  "))
    area_square = (side * side)
    print()
    print("The area of your square is " + str(area_square))
    print()

    try_again = input("Do you wish to solve another area problem:  ")
    print()
    if try_again == "yes" or try_again == "Yes" or try_again == "y":
        start()
    else:
        end()


def triangle():  # Triangle
    side1 = float(input("What is the first side of your triangle:  "))
    print()
    side2 = float(input("What is the second side of your triangle:  "))
    print()
    side3 = float(input("What is the third side of your triangle:  "))
    print()
    area_triangle = (side1 * side2 * side3) / 2
    print("The area of your triangle is " + str(area_triangle))
    print()
    try_again = input("Do you wish to solve another area problem:  ")
    print()
    if try_again == "yes" or try_again == "Yes" or try_again == "y":
        start()
    else:
        end()


def end():  # Ending
    print("This is the end of the program - Jordan Leich")
    print()
    quit()


# Main Engine
start()
