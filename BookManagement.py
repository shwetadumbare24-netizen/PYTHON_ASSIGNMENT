class Book:

    def __init__(self, Book_name, Book_Id, Author_name):
        self.Book_name = Book_name
        self.Book_Id = Book_Id
        self.Author_name = Author_name
        self.available = True

    def display_book(self):
        print("\n-------- Book Details --------")
        print("Book Name:", self.Book_name)
        print("Book ID:", self.Book_Id)
        print("Author Name:", self.Author_name)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def check_Availability(self):
        if self.available:
            print("Book is Available.")
        else:
            print("Book is Issued.")


# List to store many book objects
books = []


while True:

    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Check Availability")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            # Add Book
            Book_name = input("Enter Book Name: ")
            Book_Id = int(input("Enter Book ID: "))
            Author_name = input("Enter Author Name: ")

            book = Book(Book_name, Book_Id, Author_name)
            books.append(book)

            print("Book added successfully.")

        case 2:
            # Display All Books
            if len(books) == 0:
                print("No books available.")
            else:
                for book in books:
                    book.display_book()

        case 3:
            # Issue Book
            Book_Id = int(input("Enter Book ID: "))

            found = False

            for book in books:
                if book.Book_Id == Book_Id:
                    book.issue_book()
                    found = True
                    break

            if not found:
                print("Book ID not found.")

        case 4:
            # Return Book
            Book_Id = int(input("Enter Book ID: "))

            found = False

            for book in books:
                if book.Book_Id == Book_Id:
                    book.return_book()
                    found = True
                    break

            if not found:
                print("Book ID not found.")

        case 5:
            # Check Availability
            Book_Id = int(input("Enter Book ID: "))

            found = False

            for book in books:
                if book.Book_Id == Book_Id:
                    book.check_Availability()
                    found = True
                    break

            if not found:
                print("Book ID not found.")

        case 6:
            print("Thank you for using Library Management System.")
            break

        case _:
            print("Invalid choice.")