contacts = {}

def show_contacts():
    if not contacts:
        print("Your contact book is empty.\n")
        return
    print("\nYour contacts:")
    for name, info in contacts.items():
        print(f"{name}: {info}")
    print()

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added {name}\n")

def remove_contact():
    name = input("Enter the name to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Removed {name}\n")
    else:
        print("That name isn't in your contacts.\n")

def search_contact():
    name = input("Enter the name to search for: ")
    if name in contacts:
        print(f"\n{name}: {contacts[name]}\n")
    else:
        print("That name isn't in your contacts.\n")

print("Contact Book")
print("Commands: add, remove, search, view, quit\n")

while True:
    command = input("What do you want to do? ").lower()

    if command == "add":
        add_contact()
    elif command == "remove":
        remove_contact()
    elif command == "search":
        search_contact()
    elif command == "view":
        show_contacts()
    elif command == "quit":
        print("See you next time")
        break
    else:
        print("Not a valid command, try add, remove, search, view, or quit\n")