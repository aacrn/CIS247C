#Aaron Truong
# Exam 2 CIS 247 C

"""
1. Add a book with a specified number of copies.
2. Find a book by title and display the number of copies available.
3. Remove a book by title, reducing the number of copies by one.
If the number of copies reaches zero, prompt the user to either keep the book in the system or remove it completely.
4. Quit the program, saving the inventory to the text file.
"""

import os

def load_books(filename):
    books = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                title, copies = line.strip().split(',')
                books[title] = int(copies)
    return books

def save_books(filename, books):
    with open(filename, 'w') as file:
        for title, copies in books.items():
            file.write(f"{title},{copies}\n")

def add_book(books):
    title = input("Enter the book title to add: ")
    try:
        copies = int(input(f"How many copies of '{title}' are you adding? "))
        if copies < 0:
            print("Cannot add a negative number of copies.")
            return
        if title in books:
            books[title] += copies
        else:
            books[title] = copies
        print(f"Added {copies} copies of '{title}'.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for copies.")

def find_book(books):
    title = input("Enter the book title to find: ")
    if title in books:
        print(f"There are {books[title]} copies of '{title}' in stock.")
    else:
        print(f"No copies of '{title}' are currently in stock.")

def remove_book(books):
    title = input("Enter the book title to remove: ")
    if title in books:
        if books[title] > 0:
            books[title] -= 1
            print(f"Removed 1 copy of '{title}'.")
            if books[title] == 0:
                choice = input(f"'{title}' is out of stock. Would you like to (k)eep it in the system or (r)emove it? ")
                if choice.lower() == 'r':
                    del books[title]
                    print(f"Removed '{title}' from inventory.")
        else:
            print(f"No copies of '{title}' are currently in stock.")
    else:
        print(f"'{title}' is not in the inventory.")

def main():
    filename = "library_inventory.txt"
    books = load_books(filename)

    while True:
        print("\nLibrary Inventory System")
        print("1. Add a book")
        print("2. Find a book")
        print("3. Remove a book")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            find_book(books)
        elif choice == '3':
            remove_book(books)
        elif choice == '4':
            save_books(filename, books)
            print("Inventory saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    save_books(filename, books)

main()