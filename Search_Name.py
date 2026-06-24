# List of names
names = ["Neel", "Alex", "Sophia", "Liam", "Emma"]

# Main loop
while True:
    print("\n--- Name Search Project ---")
    print("1. View Names")
    print("2. Search Name")
    print("3. Add Name")
    print("4. Remove Name")
    print("5. Sort Names")
    print("6. Exit")

    choice = input("Choose an option: ")

    # View names
    if choice == "1":
        print("\nNames:")
        for name in names:
            print(name)

    # Search for a name
    elif choice == "2":
        search = input("Enter name to search: ")

        if search in names:
            print(search, "was found!")
        else:
            print(search, "was NOT found.")

    # Add a name
    elif choice == "3":
        new_name = input("Enter new name: ")
        names.append(new_name)
        print(new_name, "was added.")

    # Remove a name
    elif choice == "4":
        remove_name = input("Enter name to remove: ")

        if remove_name in names:
            names.remove(remove_name)
            print(remove_name, "was removed.")
        else:
            print("Name not found.")

    # Sort names
    elif choice == "5":
        names.sort()
        print("Names sorted!")

    # Exit program
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")