#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:23:50 2024

@author: devin
"""

import math

# Math Operations Class
class BasicMathOperations:
    # No constructor needed - empty constructor by default will do
    
    # Method to greet users
    # Takes in a first name and last name
    def greetUser(self, firstName, lastName):
        # Print the greeting
        print("Welcome, " + str(firstName), lastName + "!")
        
    # Method to add numbers
    # Takes in two numbers
    def addNumbers(self, num1, num2):
        # Returns their sum
        return(num1+num2)
    
    # Method to perform a specified operation
    # Takes in 2 numbers and an operation 
    def performOperation(self, num1, num2, operation):
        # Based on the sent in operation, return the worked out answer
        if operation == "multiplication":
            return(num1 * num2)
        elif operation == "division":
            return(num1/num2)
        elif operation == "addition":
            return(num1+num2)
        elif operation == "subtraction":
            return(num1-num2)
        # If the user inputs something other than the 4 operations programmed, throw an error
        else:
            print("Invalid operation. Please try again")
        
    # Method for squaring a given number
    def square(self, num):
        return(num**2)
        
    # Method for calculating a given number's factorial
    def factorial(self,num):
        # 0! is 1, and our way of calculating factorials would not return this
        # Thus we add a special case
        if num == 0:
            factorial = 1
        else:
            factorial = 1
            # Multiply the previous number by the next until we get up to the input number
            # So this iteration for an input of 4 returns 1*2*3*4
            for i in range (2,num+1):
                factorial *= i
        return(factorial)
            
    # Method for counting, given a start and end number
    def countNum(self,start,end):
        # Creates an empty list to store the count
        countList = []
        # If the start number is less than the end number
        if start<end:
            # Count up
            for i in range(start,end+1):
                # Append each successive value to the count list
                countList.append(i)
        # If it's greater
        else:
            # Count down
            for i in range(start,end-1,-1):
                countList.append(i)
        return(countList)
    
    # Method for finding the hypotenuse of a right triangle
    def hypotenuse(self,leg1,leg2):
        # Run the square method on the two input legs (base and perp)
        leg1square = self.square(leg1)
        leg2square = self.square(leg2)
        # Take the square root of the sum of those two values
        hypotenuse = math.sqrt(leg1square + leg2square)
        return(hypotenuse)
    
    # Method for finding the area of a rectangle
    def rectArea(self,width,height):
        # Multiply width and height
        return(width*height)
    
    # Method for raising a number to a power
    def power(self,base,power):
        # Raise the base to the input power
        return(base**power)
    
    # Method for checking the type of an input
    def typeCheck(self,inVar):
        # Returns the type of the input 
        return(type(inVar))
    
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
        # Allow the user to input the number of the function they want to use
        choice = eval(input("Please enter the number of the function you want to use: "))
        # Creates an object from the BasicMathOperations class
        mathObject = BasicMathOperations()
        # Greet user
        if choice == 1:
            # Takes in required inputs
            firstName = input("Please enter your first name: ")
            lastName = input ("Please enter your last name: ")
            # Invokes the method
            mathObject.greetUser(firstName, lastName)
        # Add numbers
        elif choice == 2:
            # Takes in num1 and num2 as a tuple
            numTup = eval(input("Please input 2 numbers, separated by commas: "))
            # Invokes the method
            addNum = mathObject.addNumbers(numTup[0], numTup[1])
            # Prints the result to 2 decimal places
            print(f"{numTup[0]} + {numTup[1]} = {addNum:.2f}")
        # Perform operation 
        elif choice == 3:
            # Takes in num1 and num2 as a tuple
            numTup = eval(input("Please input 2 numbers, separated by commas: "))
            # Takes in operation as a string
            operation = input("What operation would you like? ").casefold()
            # Invokes the method
            performed = mathObject.performOperation(numTup[0],numTup[1],operation)
            # Prints the result rounded to 2 decimal places
            print(f"The answer is: {performed:.2f}")
        # Square number
        elif choice == 4:
            # Takes in the number to be squared
            numIn = eval(input("What number would you like squared? "))
            # Invokes the method
            squared = mathObject.square(numIn)
            # Prints the number squared rounded to 2 decimal places
            print(f"{numIn} squared is {squared:.2f}")
        # Factorial
        elif choice == 5:
            # Takes in an INTEGER to find the factorial of
            factNum = int(input("What integer would you like the factorial of? "))
            # Only invokes the method if the integer is non-negative
            if factNum >= 0:
                fact = mathObject.factorial(factNum)
                # Prints the result
                print(f"{factNum}! = {fact}")
            # Throws an error if the integer input is negative
            else:
                print("You can't take the factorial of a negative")
        # Counting
        elif choice == 6:
            # Take in the start and end numbers--they must be integers
            start = int(input("Please enter an integer to be the start number: "))
            end = int(input("Please enter an integer to be the end number: "))
            # Invokes the method and prints
            count = mathObject.countNum(start,end)
            print(count)
        # Hypotenuse
        elif choice == 7:
            # Takes in two legs of the right triangle as a tuple
            numTup = eval(input("Please input the two legs of the right triangle, separated by commas: "))
            # Invokes the method
            hypot = mathObject.hypotenuse(numTup[0],numTup[1])
            # Prints the result rounded to 2 decimal places
            print(f"The hypotenuse of a right triangle with legs {numTup[0]} and {numTup[1]} is {hypot:.2f}")
        # Rectangle Area
        elif choice == 8:
            # First prints a sample invoking the method with VALUES
            print(f"Sample: the area of a rectangle with width 3 and height 2 is {mathObject.rectArea(3,2)}")
            # Takes in user input width and height
            width = eval(input("Please enter the width of the rectangle: "))
            height = eval(input("Please enter the height of the rectangle: "))
            # Invokes the method with VARIABLES
            area = mathObject.rectArea(width,height)
            # Prints result
            print(f"The area of a rectangle with width {width} and height {height} is {area:.2f}")
        # Number Power
        elif choice == 9:
            # Takes in a base and a power as inputs
            base = eval(input("Please enter the base number (the number being raised to a power): "))
            power = eval(input("Please enter the power to raise the base to: "))
            # Invokes the method
            expon = mathObject.power(base,power)
            # Prints result rounded to two decimal places
            print(f"({base})^{power} = {expon:.2f}")
        # Type
        elif choice == 10:
            # Accepts an argument. Uses eval to have python convert it to correct datatype
            arg = eval(input("Please type whatever you want to know the data type of: "))
            # Invokes the method
            typeArg = mathObject.typeCheck(arg)
            # Prints the result
            print(typeArg)
        # If user types anything other than 1-10, throw error
        else:
            print("Invalid choice. Please try again!")

                
main()