#!/usr/bin/env python3
# Author: Teminxit
# Program Name: ReCalc
# Python Version: Python3
# OS: Windows 10 Home, Linux (Ubuntu 16.04 LTS)

# Modules

import os
import sys
import time
from time import sleep

__version__ = "1.0"  # Version for the program
__author__ = "Teminxit"  # Name of the author


# Functions / If Statements / Calculation

# 1st Function (Instructions) - This will give the user instructions of this program.

def Instructions():
    os.system('cls')
    os.system('color 0B')
    INSTRUCTIONS = ("""

This is a basic calculator, that supports all of the operations that Python has to offer.

Operators Supported By ReCalc:


#=================#
# + - * / % ** // #
#=================#

Mathmetical Operation Names:

* Addition        = (+)
* Subtraction     = (-)
* Multiplication  = (*)
* Division        = (/)
* Modulus         = (%)
* Exponentiation  = (**)
* Floor Division  = (//)


Examples:

Addition: 10 + 2 = 12
Subtraction: 10 - 2 = 8
Multiplication: 9 * 4 = 36
Division = 10 / 2 = 5.0
Modules: 8 % 3 = 0
Exponentiation: 7 ** 2 = 49
Floor Division: 25 // 2 = 12
""")
    for x in INSTRUCTIONS:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)

    ReCalc = input("\nPress (R) To Start ReCalc: ")
    if ReCalc == 'r' or ReCalc == 'R':
        main()
    else:
        print("\nInvalid Input!")
        time.sleep(2)
        os.system('cls')
        print("\t\n\nLoading.")
        time.sleep(1.5)
        os.system('cls')
        print("\t\n\nLoading..")
        time.sleep(1.5)
        os.system('cls')
        print("\t\n\nLoading...")
        time.sleep(1.5)
        os.system('cls')
        main()


# 2nd Function (main) - This is the main function of this program. (Everything is lead by this function).      

def main():
    os.system(f"title ReCalc v{__version__} by: {__author__}")
    os.system('cls')
    os.system('color 0A')
    START_CALC = input("Press (R) To Start ReCalc\nPress (I) To View Instructions: ")
    if START_CALC == 'i' or START_CALC == 'I':
        Instructions()
    elif START_CALC == 'r' or START_CALC == 'R':
        Calculator()
    else:
        print("\nInvalid Input!")
        time.sleep(1.5)
        os.system('cls')
        main()


# 3rd Function (Calculator) - This is the function for calculating Mathematical Operations.

def Calculator():
    time.sleep(0.5)
    os.system('cls')
    global num1, op, num2
    num1 = int(input("Enter first number: "))
    time.sleep(0.1)
    os.system('cls')
    op = input("Enter operator: ")
    time.sleep(0.1)
    os.system('cls')
    num2 = int(input("Enter second number: "))
    time.sleep(0.1)
    os.system('cls')
    if op == '-':
        Subtraction()
    elif op == '+':
        Addition()
    elif op == '*':
        Multiplication()
    elif op == '/':
        Division()
    elif op == '**':
        Exponentiation()
    elif op == '//':
        FloorDivision()
    elif op == '%':
        Modulus()
    else:
        Error()


# 4th Function (Subtraction) - Function for subtracting 2 numbers.

def Subtraction():
    print(f"{num1} {op} {num2} = ", num1 - num2)
    INPUT()


# 5th Function (Addition) - Function for adding 2 numbers.

def Addition():
    print(f"{num1} {op} {num2} = ", num1 + num2)
    INPUT()


# 6th Function (Multiplication) - Function for multiplying 2 numbers.

def Multiplication():
    print(f"{num1} {op} {num2} = ", num1 * num2)
    INPUT()


# 7th Function (Division) - Function for dividing 2 numbers.

def Division():
    print(f"{num1} {op} {num2} = ", num1 / num2)
    INPUT()


# 8th Function (Exponentiation) - Function to exponentiate 2 numbers.

def Exponentiation():
    print(f"{num1} {op} {num2} = ", num1 ** num2)
    INPUT()


# 9th Function (Modulus) - Function to return the remainder of dividing the left-hand operand by right-hand operand.

def Modulus():
    print(f"{num1} {op} {num2} = ", num1 % num2)
    INPUT()


# 10th Function (FloorDivision) - Function to divide or round the number down to the nearest integer.

def FloorDivision():
    print(f"{num1} {op} {num2} = ", num1 // num2)
    INPUT()


# 11th Function (INPUT) - Function to give the user an input for: (Exitting the program), (Calculating Again), (Viewing Instructions).

def INPUT():
    Var = input("\nPress (E) to Exit" \
                "\nPress (A) to Calculate Again" \
                "\nPress (V) to View The Instructions\n")
    if Var == 'a' or Var == 'A':
        Calculator()
    elif Var == 'v' or Var == 'V':
        Instructions()
    elif Var == 'e' or Var == 'E':
        sys.exit()
        exit(0)
    else:
        print("Invalid Input")
        os.system('cls')
        time.sleep(1.0)
        main()
        


# 12th Function (Error) - Function that will activate if the user has input an invalid operator.

def Error():
    print("Invalid Operator!")
    time.sleep(2.5)
    Calculator()


if __name__ == '__main__':  # Calling main function
    main()
