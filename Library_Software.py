class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()  # String
        self.author = author  # String
        self.dewey = dewey  # String
        self.isbn = isbn  # String
        self.available = True
        self.borrower = None
        book_list.append(self)  # Holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("############################")


class User:
    def __init__(self, name, address):
        self.name = name  # String
        self.address = address  # String
        self.fees = 0.0  # Float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees $", self.fees)
        print("############################")


# Main Routine
book_list = []
user_list = []

# Create book objects
Book("Lord Of The Rings", "J.R.R Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", "97818532262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

# Create user objects
User("Johnny", "12 Maryland st")
User("Bill", "107 Happytime rd")
User("Maximillion", "107 Saddness rd")
User("Leonard", "99 Building av")


def print_info():
    for book in book_list:
        book.book_details()


def print_user():
    for user in user_list:
        user.user_details()


# Add a new library user
def add_user():
    name = input("Enter in the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address, "has been added to the user list")


# Add a new book
def add_book():
    title = input("Enter in the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey code: ").upper()
    isbn = input("Enter the new book's ISBN: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list.")


# Find a user
def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name.")
    return None


# Find a book
def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry, no book was found with that name.")
    return None


# Lend a book function
def lend_book():
    user = find_user()
    print()
    if user:  # Only if user was found
        book = find_book()  # Make sure the book exists
        if book.available:  # And is available
            confirm = input("Type 'Y' if you want to borrow this "
                            "book: ").upper()  # User confirms
            if confirm == "Y":
                print(f"Book title: '{book.title}' is now out on "
                      f"loan to {user.name}.")  # Feedback to user
                book.available = False  # Set 'available' attribute
                book.borrower = user.name  # Record borrower name
                user.borrowed_books.append(book.title)
        else:
            print(f"Sorry, '{book.title}' is already out on loan.")


# Returning a book
def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to return this "
                            "book: ").upper()  # User confirms
            if confirm == "Y":
                print(f"Book title: '{book.title}' is now returned to the  "
                      f"library.")
                book.available = True
                book.borrower = user.name
                user.borrowed_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' out on loan to someone else.")


# User menu
new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nWhat would you like to do? - enter a number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        confirm = input("Type 'Y if you want to exit the system - or any other"
                        " key to go back to the menu").upper()
        if confirm == "Y":
            print("Goodbye")
            new_action = False
    else:
        print("\n**** That was not a valid choice ***\n")

# Print_info()
lend_book()
print("\n*********************************\n")
return_book()
find_book()
find_user()
add_book()
add_user()
print_user()
