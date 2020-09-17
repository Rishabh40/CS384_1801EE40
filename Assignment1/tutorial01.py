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
    if isinstance(num2, float) and num2 == int(num2):
        num2 = int(num2)
    if isinstance(num1, (int, float)) and isinstance(num2, int):
        if num1 == 0:
            return 0
        elif num2 < 0:
            return 1/power(num1, -1*num2)
        if num2 == 0:
            return 1
        elif num2 % 2 == 0:
            return power(num1, num2//2)*power(num1, num2//2)
        else:
            return num1*power(num1, num2//2)*power(num1, num2//2)
    else:
        return 0


# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
    if isinstance(n, float) and int(n) == n:
        n = int(n)
    if isinstance(a, (int, float)) and isinstance(r, (int, float)) and isinstance(n, int) and n >= 0:
        gp = []
        curr_term = a
        for i in range(0, n):
            gp.append(curr_term)
            curr_term = r * curr_term
        return gp
    else:
        return [0]


# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
    if isinstance(n, float) and int(n) == n:
        n = int(n)
    if isinstance(a, (int, float)) and isinstance(d, (int, float)) and isinstance(n, int) and n >= 0:
        ap = []
        curr_term = a
        for i in range(0, n):
            ap.append(curr_term)
            curr_term = curr_term + d
        return ap
    else:
        return [0]


# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
    if isinstance(n, float) and int(n) == n:
        n = int(n)
    if isinstance(a, (int, float)) and isinstance(d, (int, float)) and isinstance(n, int) and n >= 0:
        hp = []
        curr_term = a
        for i in range(0, n):
            if curr_term == 0:
                return [0]
            hp.append(round(1/curr_term, 3))
            curr_term = curr_term + d
        return hp
    else:
        return [0]
