phonebook = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Display all contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"{name} added to phonebook.")

    elif choice == "2":
        name = input("Enter name to search: ")
        print(phonebook.get(name, "Not found"))

    elif choice == "3":
        for name, number in phonebook.items():
            print(f"{name}: {number}")

    elif choice == "4":
        name = input("Name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"{name} deleted")
        else:
            print("Not found")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")