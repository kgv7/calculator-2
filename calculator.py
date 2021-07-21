"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

def calculate_numbers(input):
    # repeat forever:
    while True:
#     read input
        operation = input
#     tokenize input
        output = operation.split(" ")
        num1 = float(output[1])

        if len(output) < 3:
            num2 = "0"
        else:
            num2 = float(output[2])
        # print(output)
        if output[0] == "q":
            break
        else:
            if output[0] == "pow":
                return power(num1, num2)
            elif output[0] == "+":
                return add(num1, num2)
            elif output[0] == "-":
                return subtract(num1, num2)
            elif output[0] == "*":
                return multiply(num1, num2)
            elif output[0] == "/":
                return divide(num1, num2)
            elif output[0] == "square":
                return square(num1)
            elif output[0] == "cube":
                return cube(num1)
            elif output[0] == "mod":
                return mod(num1, num2)

print(calculate_numbers("square 3.4"))
