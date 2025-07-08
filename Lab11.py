#Aaron Truong
# Lab 11 CIS 247 C

from Contact import Contact
import pickle


def load_contacts():
   """ Unpickle the data on mydata.dat and save it to a dictionary
   Return an empty dictionary if the file doesn't exist """
   try:
      with open("mydata.dat", 'rb') as file:
         return pickle.load(file)
   except FileNotFoundError:
      return {}


def save_contacts(contacts):
   """ Serialize and save the data in the 'contacts' dictionary """
   with open("mydata.dat", 'wb') as file:
      pickle.dump(contacts, file)


def add(contacts):
   """ Ask the user to add a contact to the 'contacts' dictionary
   Do not allow duplicate names """
   name = input("Name: ")
   if name in contacts:
      print("An entry already exists for that contact!")
      return

   email = input("Email: ")
   entry = Contact(name, email)

   # Add phone numbers to the new Contact object until the user decides to stop
   while True:
      next_num = input("Enter a phone number (or -1 to stop): ")
      if next_num == "-1":
         break
      entry.add_number(next_num)

   # Add the new Contact object to the dictionary
   contacts[name] = entry


def look_up(contacts):
   """ Print the information related to the given name (if it exists in the dictionary) """
   name = input("Enter a name: ")
   if name in contacts:
      print(contacts[name])
   else:
      print("There is no contact with that name")


def delete(contacts):
   """ Delete the contact associated with the name the user enters (if it exists in the dictionary) """
   name = input("Enter a name to remove from your list of contacts: ")
   if name in contacts:
      print("Are you sure you want to delete the following contact? ")
      print(contacts[name])
      choice = input("'y' or 'n': ")
      if choice == 'y':
         del contacts[name]
      else:
         print("Contact saved in dictionary")
   else:
      print("There is no contact with that name")


def edit_contact(contacts):
   """ Edit an existing contact's phone numbers, email, or name """
   name = input("Enter the name of the contact to edit: ")
   if name not in contacts:
      print("There is no contact with that name")
      return

   contact = contacts[name]
   while True:
      print("\nEditing Contact:")
      print(contact)
      print("\nWhat would you like to do?")
      print("1) Remove a phone number")
      print("2) Add a phone number")
      print("3) Change email address")
      print("4) Change contact's name")
      print("5) Stop editing")
      choice = input("Enter your choice (1-5): ").strip()
      if choice == '1':
         if not contact.phone_numbers:
            print("No phone numbers to remove.")
         else:
            print("Phone numbers:")
            for idx, num in enumerate(contact.phone_numbers, 1):
               print(f"{idx}) {num}")
            try:
               num_choice = int(input("Enter the number of the phone to remove: "))
               if 1 <= num_choice <= len(contact.phone_numbers):
                  contact.remove_number(contact.phone_numbers[num_choice - 1])
                  print("Phone number removed.")
               else:
                  print("Invalid selection.")
            except ValueError:
               print("Invalid input.")
      elif choice == '2':
         new_num = input("Enter the new phone number: ")
         contact.add_number(new_num)
      elif choice == '3':
         new_email = input("Enter the new email address: ")
         contact.email = new_email
         print("Email updated.")
      elif choice == '4':
         new_name = input("Enter the new name: ")
         if new_name in contacts:
            print("A contact with that name already exists.")
         else:
            contact.name = new_name
            contacts[new_name] = contact
            contacts.pop(name)
            name = new_name  # update name for further edits
            print("Name updated.")
      elif choice == '5':
         print("Finished editing contact.")
         return
      else:
         print("Invalid choice. Please enter 1-5.")


def main():
   contacts = load_contacts()

   ### Ask the user what to do next each loop iteration
   while True:
      choice = int(input("\nEnter 1) to add a contact, 2) to lookup a contact, "
                  "3) to delete a contact, 4) to edit a contact, 5) to quit: "))
      if choice == 1:
         add(contacts)
      elif choice == 2:
         look_up(contacts)
      elif choice == 3:
         delete(contacts)
      elif choice == 4:
         edit_contact(contacts)
      elif choice == 5:
         break

   save_contacts(contacts)


main()