#!/usr/bin/env python
#Just a Calcultaor Challenge
def calulator_choice():
    choice = str(input(f"Do you need to\n(1). Add\n(2). Subtract\n(3). Multiply\n(4). Divide\n"
                   f"Please enter the number of your choice: "))
    if(choice == "1" or choice == "1 "):
        add()
    elif(choice == "2" or choice == "2 "):
        sub()
    elif(choice == "3" or choice == "3 "):
        mult()
    elif(choice == "4" or choice == "4 "):
        div()
    else:
        print("This is not a valid Input. Please try again")
        calulator_choice()

def add():
    while True:
        try:
            x = float(input(f"Enter the 1st number you wish to Add: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    while True:
        try:
            y = float(input(f"Enter the 2nd number you wish to Add: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    print(x + y)
    calc_again()

def sub():
    while True:
        try:
            x = float(input(f"Enter the 1st number you wish to Subtract: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    while True:
        try:
            y = float(input(f"Enter the 2nd number you wish to Subtract: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    print(x - y)
    calc_again()

def mult():
    while True:
        try:
            x = float(input(f"Enter the 1st number you wish to Multiply: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    while True:
        try:
            y = float(input(f"Enter the 2nd number you wish to Multiply: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    print(x * y)
    calc_again()

def div():
    while True:
        try:
            x = float(input(f"Enter the 1st number you wish to Divide: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    while True:
        try:
            y = float(input(f"Enter the 2nd number you wish to Divide: "))
            break
        except ValueError:
            print(f"This is not a number. Try again.")
    print(x/y)
    calc_again()

def calc_again():
    again = str(input(f"Do you need to calculate any other numbers? y or n: "))
    if(again.lower() == "y" or again.lower() == "y "):
        calulator_choice()
    elif(again.lower() == "n" or again.lower() == "n "):
        print("Have a good day!")
    else:
        print(f"That is not a valid input please try again")


print("Welcome to THE CALCULATOR")
calulator_choice()
