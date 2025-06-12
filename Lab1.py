#Aaron Truong
# CIS 247 Lab 1

"""
Args
    num1 = float, First number
    num2 = float, Second number
    operation = Str, add or multiply

Return
    num1 operation num2 if operation exist, else print error message, return None
"""

def math_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        print (f'Error: {operation} "is an invalid operation."')
        return None

#defined a function which takes 3 parameters and outputs 3 possible situations


try:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = input('Enter operation: ').strip().lower()

    result = math_operation(num1, num2, operation)

    if result is not None:
        print(f'Result: {result}')

except ValueError:
    print ("Error: Number is not valid")

"""
try and except block, filters out invalid numbers

takes input from user
creates result based on function
prints if value if not None
else prints error message
"""