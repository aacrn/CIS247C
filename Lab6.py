#Aaron Truong
#Lab 6 CIS 247 C

"""
make a program that will multiply two numbers together and save the results to a file
"""

def multiply_numbers():
    while True:
        num1 = input("Enter the first number (or 'q' to quit): ")
        if num1.lower() == 'q':
            break
        num2 = input("Enter the second number (or 'q' to quit): ")
        if num2.lower() == 'q':
            break
        try:
            result = int(num1) * int(num2)
            with open("data\\results.txt", "a") as f:
                f.write(f"{num1} * {num2} = {result}\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    multiply_numbers()
    print("Multiplication results have been saved to data\\results.txt")

main()


