import json
import uuid
from datetime import datetime
from book import BookManager
from user import UserManager

class Storage:
    def __init__(self, book_file="books.json", user_file="users.json", book_in_out_file="book_in_out.json"):
        self.book_file = book_file
        self.user_file = user_file
        self.book_in_out_file = book_in_out_file

        self.book_manager = BookManager()
        self.user_manager = UserManager()

        self.book_in_out_log = []  # Initialize the log for book check-ins and check-outs

        self.load_books()
        self.load_users()
        self.load_book_in_out()

    def load_books(self):
        try:
            with open(self.book_file, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    self.book_manager.add_book(book_data['title'], book_data['author'], book_data['isbn'], book_data['books_available'])
        except FileNotFoundError:
            pass

    def save_books(self):
        books_data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'books_available': book.books_available} for book in self.book_manager.list_books()]
        with open(self.book_file, 'w') as f:
            json.dump(books_data, f, indent=4)

    def load_users(self):
        try:
            with open(self.user_file, 'r') as f:
                users_data = json.load(f)
                for user_data in users_data:
                    self.user_manager.add_user(user_data['name'], user_data['user_id'], user_data.get('mobile_num', None))  # 'mobile_num' is optional
        except FileNotFoundError:
            pass

    def save_users(self):
        users_data = [{'name': user.name, 'user_id': user.user_id, 'mobile_num': user.mobile_num} for user in self.user_manager.list_users()]
        with open(self.user_file, 'w') as f:
            json.dump(users_data, f, indent=4)

    def load_book_in_out(self):
        try:
            with open(self.book_in_out_file, 'r') as f:
                self.book_in_out_log = json.load(f)
        except FileNotFoundError:
            self.book_in_out_log = []

    def save_book_in_out(self):
        with open(self.book_in_out_file, 'w') as f:
            json.dump(self.book_in_out_log, f, indent=4)

    def log_book_in_out(self, entry):
        self.book_in_out_log.append(entry)
        self.save_book_in_out()

    # Book methods
    def add_book(self, title, author, isbn, books_available):
        self.book_manager.add_book(title, author, isbn, books_available)
        self.save_books()

    def list_books(self):
        return self.book_manager.list_books()

    def search_books(self, keyword, by='title'):
        return self.book_manager.search_books(keyword, by)

    def update_book(self, isbn= None, title = None, author = None, books_available = None):
        updated = self.book_manager.update_book(isbn, title, author, books_available)
        if updated:
            self.save_books()
        else:
            print(f"Book with ISBN {isbn} not found.")

    def delete_book(self, isbn):
        self.book_manager.delete_book(isbn)
        self.save_books()

    # User methods
    def add_user(self, name, user_id, mobile_num=None):
        self.user_manager.add_user(name, user_id, mobile_num)
        self.save_users()

    def list_users(self):
        return self.user_manager.list_users()

    def search_users(self, keyword, by='name'):
        return self.user_manager.search_users(keyword, by)

    def update_user(self, user_id, name=None,late_fees = None):
        self.user_manager.update_user(user_id, name,late_fees)
        self.save_users()

    def delete_user(self, user_id):
        self.user_manager.delete_user(user_id)
        self.save_users()

    # Book in/out logging methods
    def log_book_check_in(self, user_id, user_name, book_isbn, book_title):
        book = self.book_manager.search_books(book_isbn, by='isbn')
        if book and int(book[0].books_available) > 0:
            book = book[0]
            in_out_id = str(uuid.uuid4())  # Generate unique in_out_id
            check_in_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = {
                'in_out_id': in_out_id,
                'user_id': user_id,
                'user_name': user_name,
                'book_isbn': book_isbn,
                'book_name': book_title,
                'check_in_datetime': check_in_datetime,
                'status': 'Issued'
            }
            self.log_book_in_out(entry)
            print(f"{book_title} check-in {in_out_id}")
            self.update_book(book_isbn, books_available=int(book.books_available) - 1)
            self.save_books()
        else:
            print(f"'{book_title}' is not available in the library.")

    def log_book_check_out(self, in_out_id):
        check_out_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for entry in self.book_in_out_log:
            
            if (entry['in_out_id'] == in_out_id) and (entry["status"] =="Issued"):
                entry['check_out_datetime'] = check_out_datetime
                entry['status'] = 'Returned'
                book = self.book_manager.search_books(entry['book_isbn'], by='isbn')

                check_in_datetime = datetime.strptime(entry['check_in_datetime'], "%Y-%m-%d %H:%M:%S")
                check_out_datetime = datetime.strptime(entry['check_out_datetime'], "%Y-%m-%d %H:%M:%S")

                difference = check_out_datetime - check_in_datetime

                days_difference = difference.days

                print(days_difference)

                if int(days_difference) >7:
                    fees_late = (days_difference-7) * 10
                    entry['late_fees'] = fees_late
                if book:
                    book = book[0]
                    self.update_book(book.isbn, books_available=int(book.books_available) + 1)
                    self.save_books()
                self.save_book_in_out()
                return f"Successfully {entry['user_name']}{entry['book_name']} book is submitted"
            
            else:
                continue
        return f"This following check-out Key '{in_out_id}' book is submitted or invalid"

