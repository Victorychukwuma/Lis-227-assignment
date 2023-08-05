class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.books.append(book)

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def search_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        return results

    def search_by_ISBN(self, ISBN):
        results = [book for book in self.books if ISBN == book.ISBN]
        return results

    def display_books(self):
        print("\nLibrary Catalog:")
        print("=================")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.ISBN}\nStatus: {status}\n")
        print("=================")

# Adaptation of OPAC (Online Public Access Catalog)
class OPAC(Library):
    def __init__(self, name):
        super().__init__(name)

    def check_availability(self, title):
        book = next((book for book in self.books if title.lower() == book.title.lower()), None)
        if book:
            return book.available
        else:
            return None

# Adaptation of John Harris Library
class JohnHarrisLibrary(Library):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = {}

    def borrow_book(self, title, borrower_name):
        book = next((book for book in self.books if title.lower() == book.title.lower() and book.available), None)
        if book:
            book.available = False
            self.borrowed_books[borrower_name] = book
            return True
        else:
            return False

    def return_book(self, borrower_name):
        if borrower_name in self.borrowed_books:
            book = self.borrowed_books.pop(borrower_name)
            book.available = True
            return True
        else:
            return False

def main():
    print("Welcome to the Library Management System!")
    
    opac = OPAC("Online Public Library")
    opac.add_book("Introduction to Programming", "John Smith", "123456789")
    opac.add_book("Data Structures and Algorithms", "Jane Doe", "987654321")
    
    john_harris_library = JohnHarrisLibrary("John Harris Library")
    john_harris_library.add_book("Advanced Python Programming", "Alex Johnson", "543216789")

    while True:
        print("\nChoose an option:")
        print("1. Search for a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        choice = input("Enter the corresponding number: ")

        if choice == "1":
            search_query = input("Enter title or author: ")
            results = opac.search_by_title(search_query) + opac.search_by_author(search_query)
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.ISBN}")
                print("=================")
            else:
                print("No matching books found.")
        
        elif choice == "2":
            title = input("Enter the title of the book you want to borrow: ")
            borrower_name = input("Enter your name: ")
            if john_harris_library.borrow_book(title, borrower_name):
                print("Book borrowed successfully!")
            else:
                print("Book not available for borrowing.")
        
        elif choice == "3":
            borrower_name = input("Enter your name: ")
            if john_harris_library.return_book(borrower_name):
                print("Book returned successfully!")
            else:
                print("Book return not successful or borrower not found.")
        
        elif choice == "4":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
