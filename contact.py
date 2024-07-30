import sys
import re
contacts = {}

def is_valid_phone(phone):
    return bool(re.match(r'^\+?\d{10,15}$', phone))

def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def is_valid_address(address):
    return len(address.strip()) > 0

def add_contact():
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter contact phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number. It should be between 10 and 15 digits.")
        return

    email = input("Enter contact email: ").strip()
    if email and not is_valid_email(email):
        print("Invalid email address.")
        return

    address = input("Enter contact address: ").strip()
    if not is_valid_address(address):
        print("Address cannot be empty.")
        return

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No matching contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return
    
    print(f"Updating contact '{name}'.")
    
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    if phone and not is_valid_phone(phone):
        print("Invalid phone number. It should be between 10 and 15 digits.")
        return
    
    email = input("Enter new email (leave blank to keep current): ").strip()
    if email and not is_valid_email(email):
        print("Invalid email address.")
        return
    
    address = input("Enter new address (leave blank to keep current): ").strip()
    if address and not is_valid_address(address):
        print("Address cannot be empty.")
        return
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    
    print(f"Contact '{name}' updated successfully.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the system.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
