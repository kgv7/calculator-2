"""CLI application for a prefix-notation calculator."""

from arithmetic_fs import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

OPERATORS = ["+", "-", "*", "/", "pow", "mod", "square", "cube"]

def calculate_numbers(input):
    # repeat forever:
    while True:
#     read input
        operation = input
#     tokenize input
        output = operation.split(" ")
#     check for errors
        if output[0] not in OPERATORS:
            return("Incorrect operator.")
#     create number list from string provided,excluding the zero index
        output_list = []
        output_list.append((output[1:]))
        print(output_list)
        number_list = []
#     loop through list, then through each number in the list, to then add it into "number_list"
        for list in output_list:
            for number in list:
                new_number = float(number)
                number_list.append(new_number)
        
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
                return add(number_list)
            elif output[0] == "-":
                return subtract(num1, num2)
            elif output[0] == "*":
                return multiply(number_list)
            elif output[0] == "/":
                return divide(num1, num2)
            elif output[0] == "square":
                return square(num1)
            elif output[0] == "cube":
                return cube(num1)
            elif output[0] == "mod":
                return mod(num1, num2)

print(calculate_numbers("pow 1 2 3 4 5 6"))
