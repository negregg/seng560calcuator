#!/usr/bin/python3

# Title: Simple Calulator utilizing https://github.com/jdc0051/seng560Calc
#         library for backend functions
# Author: Nathan Gregg
# Date: 2019.10.28


"""Simple Math Calculatior written in Python3.  This calculator performs basic
math operations utilizing a library from https://github.com/jdc0051/seng560Calc.
Main purpose of program is to test reusability of said library.


"""
import sys
from os import system, name 
from seng560Calc import *

continueProcessing = True
print(80 * '*')
print("\nWelcome to the Simple Text Calculator!\n")
print(80 * '*')

#Main Function
def main ():
    print("\nPlease select from the following options/operations.")
    print("NOTE: This simple calculator can only operate on a max of two numbers.")
    print(80 * '-')
    print("1) Addition")
    print("2) Subtaction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit Program\n")
    print(80 * '-')
    
    try:
        selection = int(input("Which option would you like to choose? "))
    except:
        print("Only 1 through 5 are valid options.  Returning to Main Menu.")
        resetScreen()

    if selection < 1 or selection > 5:
        print("Only 1 through 5 are valid options.  Returning to Main Menu.")
        resetScreen()
           
    if selection == 5:
        sys.exit()
    else:
        value1 = int(input("\nEnter the first number: "))
        value2 = int(input("Enter the sencond number: "))
    
    if selection == 1:
        answer = (add(value1,value2))
    elif selection == 2:
        answer = (subtract(value1,value2))
    elif selection == 3:
        answer = (multiply(value1,value2))
    elif selection == 4:
        answer = (divide(value1,value2))
    
    print("Answer: " + str(answer))
    resetScreen()
    

def resetScreen ():
    input("\nPress 'Enter' to return to Main Menu: ")
    # Clear screen on Windows systems
    if name == 'nt': 
        _ = system('cls') 
    
    # Clear screen on Linux or OSX
    else: 
        _ = system('clear') 

    # Return to main screen
    main()
 
# Call main function
main()
