
contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}


# Function to validate phone number
def valid_phone(number):
    return number.isdigit() and len(number) == 10


# Function to check whether a number belongs to another contact
def number_exists(number, current_name=None):
    for name, data in contacts.items():
        if name != current_name and number in data["phones"]:
            return name
    return None


# 1. Add Contact
def add_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("Contact already exists!")
        return

    number = input("Enter phone number: ")

    if not valid_phone(number):
        print("Invalid number! Phone number must contain exactly 10 digits.")
        return

    owner = number_exists(number)

    if owner:
        print("Number already belongs to", owner)
        return

    email = input("Enter email: ")
    city = input("Enter city: ")

    contacts[name] = {
        "phones": [number],
        "email": email,
        "city": city
    }

    print("Contact added successfully!")


# 2. Add Another Number
def add_number():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    number = input("Enter another phone number: ")

    if not valid_phone(number):
        print("Invalid number! It must contain exactly 10 digits.")
        return

    if number in contacts[name]["phones"]:
        print("This number is already saved for this contact!")
        return

    owner = number_exists(number)

    if owner:
        print("Number already belongs to", owner)
        return

    contacts[name]["phones"].append(number)

    print("Number added successfully!")


# 3. Update Email or City
def update_contact():
    name = input("Enter contact name: ")

    if name not in contacts:
        print("Contact not found!")
        return

    print("1. Update Email")
    print("2. Update City")

    choice = input("Enter choice: ")

    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ")
        print("Email updated successfully!")

    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ")
        print("City updated successfully!")

    else:
        print("Invalid choice!")


# 4. Delete Contact
def delete_contact():
    name = input("Enter contact name: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# 5. Search Contact
def search_contact():
    search_name = input("Enter name to search: ").lower()

    found = False

    for name, data in contacts.items():
        if search_name in name.lower():
            print("\nName:", name)
            print("Phone Numbers:", data["phones"])
            print("Email:", data["email"])
            print("City:", data["city"])
            found = True

    if not found:
        print("No matching contact found!")


# 6. Reports
def reports():

    # Reverse Lookup: Number -> Name
    reverse_lookup = {
        number: name
        for name, data in contacts.items()
        for number in data["phones"]
    }

    print("\n--- REVERSE LOOKUP ---")
    number = input("Enter phone number: ")

    if number in reverse_lookup:
        print("Number belongs to:", reverse_lookup[number])
    else:
        print("Number not found!")

    # Group Contacts by City
    city_groups = {}

    for name, data in contacts.items():
        city = data["city"]

        if city not in city_groups:
            city_groups[city] = []

        city_groups[city].append(name)

    print("\n--- CONTACTS BY CITY ---")

    for city, names in city_groups.items():
        print(city, ":", names)

    # Contacts with More Than One Number
    print("\n--- CONTACTS WITH MULTIPLE NUMBERS ---")

    multiple_numbers = {
        name: data["phones"]
        for name, data in contacts.items()
        if len(data["phones"]) > 1
    }

    if multiple_numbers:
        print(multiple_numbers)
    else:
        print("No contacts have multiple numbers.")

    # Print Whole Directory Alphabetically
    print("\n--- COMPLETE DIRECTORY (ALPHABETICAL) ---")

    for name in sorted(contacts):
        data = contacts[name]

        print("\nName:", name)
        print("Phone Numbers:", data["phones"])
        print("Email:", data["email"])
        print("City:", data["city"])


# Main Menu
while True:

    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        add_number()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()

    elif choice == "6":
        reports()

    elif choice == "7":
        print("Exiting Phone Directory...")
        break

    else:
        print("Invalid choice! Please try again.")
