'''
2. Create a Library Management System using Class and Object in Python. 
What to Do 1. Create a class named Book. 
 2. Create a constructor __init__() to initialize:  o Book name  o Book ID  o Author name  o Availability status  
 3. Create a display_book() method to display book details.  
 4. Create a issue_book() method:  o Check whether the book is available.  o If available, issue the book and change its status.  o If already issued, display an appropriate message. 
 5. Create a return_book() method:  o Return the issued book.  o Change its availability status back to available. 
 6. Create a check_availability() method to display whether the book is available or issued. 
'''

class Book:
    def __init__(self,Book_name,Book_Id,Author_name):
        self.Book_name = Book_name
        self.Book_Id = Book_Id
        self.Author_name = Author_name
        self.available = True

    def display_book(self):
        print("--------Book Details--------")
        print("Book Name:",self.Book_name)
        print("Book ID:", self.Book_Id)
        print("Author Name:", self.Author_name)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issue Sucessful.")
        else:
            print("Book is already issued. ")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def check_Availability(self):
        if self.available:
            print("Book Is Available.")

        else:
            print("Book Is Not Available.")


Book1 = Book("Python Programming",1001,"Guido van Rossum")
Book1 = Book("Java Programming",1002,"Divya More")
while True: 
    print("\n ------ Library Management System----")
    print("1. Display Book Details")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Check Availability")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            Book1.display_book()
        case 2:
            Book1.issue_book()
        case 3:
            Book1.return_book()
        case 4:
            Book1.check_Availability 




    