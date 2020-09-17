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
