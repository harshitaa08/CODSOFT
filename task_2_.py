# Contact Management System
# Internship Task 2 - CODSOFT
# Created by: Harshita Shukla

# This is a simple contact management application
# where the user can add, view, search, update, and delete contacts.

contacts = []

def show_menu():
    print("\n========= CONTACT MANAGEMENT SYSTEM =========")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=============================================")

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    if name and phone:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        print(f"Contact '{name}' added successfully!")
    else:
        print("Name and Phone number are required fields.")

def view_contacts():
    if len(contacts) == 0:
        print("\nNo contacts available.")
    else:
        print("\nYour Contact List:")
        print("----------------------------")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} - {contact['phone']}")
        print("----------------------------")

def search_contact():
    keyword = input("Enter name or phone number to search: ").strip()
    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("No matching contact found.")

def update_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    try:
        index = int(input("Enter contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("\nEnter new details (leave blank to keep existing):")
            name = input(f"Name ({contacts[index]['name']}): ").strip()
            phone = input(f"Phone ({contacts[index]['phone']}): ").strip()
            email = input(f"Email ({contacts[index]['email']}): ").strip()
            address = input(f"Address ({contacts[index]['address']}): ").strip()

            if name:
                contacts[index]['name'] = name
            if phone:
                contacts[index]['phone'] = phone
            if email:
                contacts[index]['email'] = email
            if address:
                contacts[index]['address'] = address

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    if len(contacts) == 0:
        return
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Contact '{removed['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

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
        print("Thank you for using the Contact Management System!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
