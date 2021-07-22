"""Functions for common math operations. 

Take in a list containing any number of number inputs."""


def add(numlist):
    """Return the sum of the two inputs."""
    sum = 0
    for number in numlist:
        sum = sum + number
    return sum

# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""
    
#     return num1 - num2

def subtract(numlist):
    """Return the second number subtracted from the first."""
    
    subtract = numlist[0] * 2

    for number in numlist:
        subtract -= number

    return subtract

def multiply(numlist):
    """Multiply the two inputs together."""
    mult = 1

    for number in numlist:
        mult = mult * number

    return mult

def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return num1 / num2
def square(num1):
    """Return the square of the input."""

    return num1 * num1
def cube(num1):
    """Return the cube of the input."""

    return num1 * num1 * num1
def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2