# Made by Jordan Leich on 5/6/2020
"""
--DESCRIPTION--
This is a very basic and simple program that is
designed for a user to either create a timer of their
choice or the option to create a stopwatch.
"""

# Imports
import time
import os

seconds = int()
minutes = int()
hours = int()


def begin():
    userchoice1 = int(input("Would you like to make a timer(1) or a countdown stopwatch(2) or end this program(0):     "))
    if userchoice1 == 1:
        timer()
    if userchoice1 == 2:
        stopwatch()
    if userchoice1 == 0:
        forceend()
    else:
        print("Invalid Input!   ")
        time.sleep(3)
        begin()


def timer():
    seconds = int()
    minutes = int()
    hours = int()
    print("Welcome to the timer!    ")
    time.sleep(2)
    run = input("Enter R to start the timer!    ")

    while run.lower() == "r":
        if seconds > 59:
            seconds = 0
            minutes = minutes + 1
        if minutes > 59:
            minutes = 0
            hours = hours + 1
        seconds = (seconds + 1)
        print(hours, ":", minutes, ":", seconds)
        time.sleep(1)


def stopwatch():
    global whentostop
    print("Welcome to the stopwatch!")
    time.sleep(2)
    while True:
        userinput = input("Enter time to countdown in seconds:  ")
        try:
            whentostop = abs(int(userinput))
        except KeyboardInterrupt:
            break
        except:
            print("Invalid Input!")
            time.sleep(3)
            stopwatch()

        while whentostop > 0:
            m, s = divmod(whentostop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left)
            time.sleep(1)
            whentostop -= 1
        print("Stopwatch finished!")
        time.sleep(2)
        restart()


def restart():
    restartchoice = str(input("Would you like to restart this program(yes or no):    "))
    if restartchoice == 'yes':
        print("restarting program...")
        time.sleep(3)
        begin()
    if restartchoice == 'no':
        forceend()
    else:
        print("Invalid Input!")
        time.sleep(3)
        restart()


def forceend():
    print("ending program...")
    time.sleep(1)
    quit()


begin()
