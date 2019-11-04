# Simple Math Calculator

## Overview

A simple math calculator written in Python math calculator written in Python 3.
This calculator provides Text User Interface (TUI) that allows a user to do 
simple math operations such as addition, substraction, multiplication, and 
division.   This application utilizies the 
https://github.com/jdc0051/seng560Calc library to perform all backend 
operations.  

## Software Requirements

This application requires Python 3 to be installed and available within your 
operating system.  Python 3 is usually part of the base install on OS X and 
Linux.  Windows will require you do install the software from 
https://www.python.org/downloads/windows/.

## Installing the Program

To install this program simple clone the software from github to a directory
of your choice.  Example:

` git clone https://github.com/negregg/seng560calcuator.git `

You may choose to also manually download the application from: 
https://github.com/negregg/seng560calcuator/archive/master.zip

Note: All files needed for application to run are included in the repoistory
including the ` seng560Calc  ` library.

## Executing the Program

Execution of the Simple Math Calculator Program is very simple.  Please follow the 
below steps:

* Open a terminal window in your operating system of choice.
* Change your working directory to where you have downloadeded/installed the
  Simple Math Calculator program.
* Execute the Simple Math Calculator Program by typing ` python3 calculator.py `.
* Follow the instructions on screen to perform basic math operations.
* The program will continue to loop to main menu so the user can process
  additional operations if desired.  Or the user can enter 5 to exit the 
  program

### Example Execution of Program
The following shows a simple execution of the program completing ad addition
operation.

```shell
********************************************************************************

Welcome to the Simple Text Calculator!

********************************************************************************

Please select from the following options/operations.
NOTE: This simple calculator can only operate on a max of two numbers.
--------------------------------------------------------------------------------
1) Addition
2) Subtaction
3) Multiplication
4) Division
5) Exit Program

--------------------------------------------------------------------------------
Which option would you like to choose? 1

Enter the first number: 10
Enter the sencond number: 5
Answer: 15

Press 'Enter' to return to Main Menu: 
```

## Experience with Utilizing https://github.com/jdc0051/seng560Calc Library

Utilizing the external, third-party seng560Calc library was good.  The library
was very easy to incorperate into the Simple Text Calculator.  Reusing the
library was done in a "black-box" fashion.  In other words, the seng560Calc
library require no modifications to be utilized in the Simple Math Calculator.
To utilize the library, a programmer needed to simple plug in the provided 
functions and pass the required two values for the desired operation.  
Returned values from functions were always of type "int" or "float" which made it 
easy to maniuplate the response inside the Simple Math Calculator.
