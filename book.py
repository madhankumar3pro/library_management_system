class Book:
    def __init__(self, title, author, isbn,books_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.books_available = books_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, books_available:{self.books_available}"


# Storage for books
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn,books_available):
        book = Book(title, author, isbn,books_available)
        self.books.append(book)

    def list_books(self):
        return self.books

    def search_books(self, keyword, by='title'):
        try:
            if by == 'title':
                return [book for book in self.books if keyword.lower() in book.title.lower()]
            elif by == 'author':
                return [book for book in self.books if keyword.lower() in book.author.lower()]
            elif by == 'isbn':
                return [book for book in self.books if keyword.lower() in book.isbn.lower()]
            else:
                return []
        except:
            print('Please enter valid keyword and title')

    def update_book(self, isbn, title=None, author=None, books_available=None):
        try:
            for book in self.books:
                if book.isbn == isbn:
                    if title:
                        book.title = title
                    if author:
                        book.author = author
                    if books_available is not None:
                        book.books_available = books_available
                    return True
        except: 
            print('Please enter valid details')
        return False

    def delete_book(self, isbn):
        try:
            self.books = [book for book in self.books if book.isbn != isbn]
        except Exception as e:
            print(e)

