from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{title}'. Please return it within 30 days.")
                else:
                    print(f"Sorry, '{title}' is currently not available.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.available:
                    book.available = True
                    print(f"Thank you for returning '{title}'.")
                else:
                    print(f"'{title}' is already available in the library.")
                return
        print(f"Book '{title}' not found in the library.")
