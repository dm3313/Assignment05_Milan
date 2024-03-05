#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 23:03:28 2024

@author: devin
"""

import math

class BasicMathOperations:
    def greetUser(self, firstName, lastName):
        print("Welcome, " + str(firstName), lastName + "!")
        
    def addNumbers(self, num1, num2):
        return(num1+num2)
        
def main():
    instructions = """Welcome! Here are your available options to choose:
    1. Greet User: Be greeted with your full name
    2. Add Numbers: Adds two numbers
    3. Perform Operation: Performs a specified operation on two numbers
    4. Square Number: Enter a number and its square is returned
    5. Factorial: Enter a number and have its factorial returned
    6. Counting: Given a start and end number, counts from start to end
    7. Hypotenuse Calculator: Given two legs, calculates the hypotenuse
    8. Rectangle Area: Calculates the area of a rectangle
    9. Number Power: Computes a number to the power of another
    10. Type of Argument: Given an argument, returns the data type
    """
    print(instructions)
    
    while True:
        choice = eval(input("Please enter the number of the function you want to use: "))
        mathObject = BasicMathOperations()
        if choice == 1:
            firstName = input("Please enter your first name: ")
            lastName = input ("Please enter your last name: ")
            mathObject.greetUser(firstName, lastName)
        elif choice == 2:
            numTup = eval(input("Please input 2 numbers, separated by commas: "))
            addNum = mathObject.addNumbers(numTup[0], numTup[1])
            print(f"{numTup[0]} + {numTup[1]} = {addNum:.2f}")
