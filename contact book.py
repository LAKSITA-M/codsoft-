contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"{name} added to contacts.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Contact details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in contacts.")

def display_contacts():
    print("\n--- Contacts ---")
    for name, details in contacts.items():
        print(f"{name}: Phone - {details['phone']}, Email - {details['email']}")

# Menu loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")