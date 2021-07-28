class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("\nBooks present in this library are: ")
        for book in self.books:
            print(" -" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"\nYou have been issued {bookName}. Please return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("\nSorry, this book is not available or has already been issued by someone else.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for reading this book!")

class Student:
    
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book
    
if __name__ == "__main__":
    centralLibrary = Library(["Algo", "Django", "Python", "Flutter"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        welcomeMsg = '''
        -=-=-Welcome to Central Library-=-=-
              Please choose an option:
               1. List all the books
               2. Request a book
               3. Add/Return a book
               4. Exit the Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for coming. Have a great day!")
            exit()
        else:
            print("Invalid Choice")             
