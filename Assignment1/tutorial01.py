# Function to add two numbers
def add(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        addition = num1+num2
    elif isinstance(num1, str) and isinstance(num2, str):
        addition = num1+num2
    else:
        addition = 0
    return addition


# Function to subtract two numbers
def subtract(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        subtraction = num1 - num2
    else:
        subtraction = 0
    return subtraction


# Function to multiply two numbers
def multiply(num1, num2):
    # Multiplication Logic
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        multiplication = num1*num2
    elif isinstance(num1, int) or isinstance(num2, int):
        multiplication = num1*num2
    else:
        multiplication = 0
    return multiplication


# Function to divide two numbers
def divide(num1, num2):
    # DivisionLogic
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num2 == 0:
            return 0
        division = num1/num2
    else:
        division = 0
    return division


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):  # num1 ^ num2
    # DivisionLogic
    return power


# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
    gp = []
    return gp


# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
    ap = []
    return ap


# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
    hp = []
    return hp
