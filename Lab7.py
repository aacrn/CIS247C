#Aaron Truong
#Lab 7 CIS 247 C

"""
Option 1: Lookup name based on ID number
Option 2: Lookup ID based on full name
Option 3: Quit
"""

def lookup_employee(employee_id):
    try:
        with open("data\\employees.txt", "r") as file:
            for line in file:
                parts = line.strip().split()
                if parts and parts[0] == str(employee_id):
                    return " ".join(parts[1:])
        return "Employee not found"
    except FileNotFoundError:
        return "Employee file not found"
    
def lookup_id(full_name):
    try:
        with open("data\\employees.txt", "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) > 1 and " ".join(parts[1:]) == full_name:
                    return parts[0]
        return "ID not found"
    except FileNotFoundError:
        return "Employee file not found"

def get_employee_id():
    while True:
        try:
            employee_id = int(input("Enter employee ID: "))
            return employee_id
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        print("\nMenu:")
        print("1. Lookup name based on ID number")
        print("2. Lookup ID based on full name")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            employee_id = get_employee_id()
            result = lookup_employee(employee_id)
            print(result)
        elif choice == "2":
            full_name = input("Enter full name (first middle last): ")
            result = lookup_id(full_name)
            print(result)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

main()