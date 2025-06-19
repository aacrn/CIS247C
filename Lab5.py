#Aaron Truong
#Lab 5 CIS 247 C

"""
Create 3 Input Functions to get a name, email, and calculate a random company ID.
Then create a function to call the 3 input functions and return the values to main.
Finally, print the values in main.
"""

import random

def get_name():
    name = input("Enter your name: ")
    return name

def get_email():
    email = input("Enter your Email: ")
    return email

def calculate_id():
    return random.randint(1000, 9999)

def get_account():
    name = get_name()
    email = get_email()
    company_id = calculate_id()
    return name, email, company_id

def main():
    name, email, company_id = get_account()
    print(f"\nName: {name}\nEmail: {email}\nCompany ID: {company_id}")

main()