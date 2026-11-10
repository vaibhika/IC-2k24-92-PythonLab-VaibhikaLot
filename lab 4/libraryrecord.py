 
# Library Record System using Nested Dictionaries

books = {
    "B1": {
        "title": "Python Basics",
        "author": "Rao",
        "copies": 2,
        "issued_to": []
    },
    "B2": {
        "title": "Data Structures",
        "author": "Iyer",
        "copies": 1,
        "issued_to": []
    },
    "B3": {
        "title": "Algorithms",
        "author": "Rao",
        "copies": 1,
        "issued_to": []
    }
}


# Function to Add Book
def add_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        copies = int(input("Enter additional copies: "))

        if copies <= 0:
            print("Copies must be greater than 0!")
            return

        books[isbn]["copies"] += copies
        print("Book copies added successfully!")

    else:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        if copies <= 0:
            print("Copies must be greater than 0!")
            return

        books[isbn] = {
            "title": title,
            "author": author,
            "copies": copies,
            "issued_to": []
        }

        print("Book added successfully!")


# Function to Issue Book
def issue_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    # Check whether member already has this book
    if member in books[isbn]["issued_to"]:
        print("Rejected! Member already holds this book.")
        return

    # Count total books held by this member
    count = 0

    for book in books.values():
        if member in book["issued_to"]:
            count += 1

    # Member can hold maximum 2 books
    if count >= 2:
        print("Rejected! Member cannot hold more than 2 books.")
        return

    # Check book availability
    if books[isbn]["copies"] <= 0:
        print("Rejected! No copies available.")
        return

    # Issue the book
    books[isbn]["copies"] -= 1
    books[isbn]["issued_to"].append(member)

    print("Book issued successfully!")
    print("Remaining copies:", books[isbn]["copies"])


# Function to Return Book
def return_book():
    isbn = input("Enter ISBN: ")
    member = input("Enter member ID: ")

    if isbn not in books:
        print("Book not found!")
        return

    if member not in books[isbn]["issued_to"]:
        print("Rejected! This member does not hold this book.")
        return

    # Return the book
    books[isbn]["issued_to"].remove(member)
    books[isbn]["copies"] += 1

    print("Book returned successfully!")
    print("Available copies:", books[isbn]["copies"])


# Function to Search Book
def search_book():
    isbn = input("Enter ISBN: ")

    if isbn in books:
        print("\nBook Details:")
        print("ISBN:", isbn)
        print("Title:", books[isbn]["title"])
        print("Author:", books[isbn]["author"])
        print("Available Copies:", books[isbn]["copies"])
        print("Issued To:", books[isbn]["issued_to"])

    else:
        print("Book not found!")


# Function to Display Reports
def reports():

    # 1. Books by a given author
    author = input("Enter author name: ")

    author_books = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["author"].lower() == author.lower()
    }

    print("\nBooks by", author, ":")
    print(author_books)


    # 2. Members holding more than one book
    member_books = {}

    # Invert book-wise data into member-wise data
    for isbn, book in books.items():

        for member in book["issued_to"]:

            if member not in member_books:
                member_books[member] = []

            member_books[member].append(book["title"])

    multiple_books = {
        member: titles
        for member, titles in member_books.items()
        if len(titles) > 1
    }

    print("\nMembers holding more than one book:")
    print(multiple_books)


    # 3. Books currently unavailable
    unavailable = {
        isbn: book["title"]
        for isbn, book in books.items()
        if book["copies"] == 0
    }

    print("\nBooks currently unavailable:")
    print(unavailable)


    # 4. Books that have never been issued
    never_issued = {
        isbn: book["title"]
        for isbn, book in books.items()
        if len(book["issued_to"]) == 0
    }

    print("\nBooks never issued:")
    print(never_issued)


# Main Menu
while True:

    print("\n===== LIBRARY RECORD SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Reports")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        issue_book()

    elif choice == 3:
        return_book()

    elif choice == 4:
        search_book()

    elif choice == 5:
        reports()

    elif choice == 6:
        print("Exiting Library Record System. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")

 