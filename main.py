import sys
from logins import MANAGER_CREDENTIALS
from storage import Storage
from getpass import getpass
import hashlib

def login():
    """
    Function to authenticate the manager login using username and password.
    """
    print("Manager Login")
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username == MANAGER_CREDENTIALS['username'] and hashed_password == MANAGER_CREDENTIALS['password']:
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def main():
    """
    Main function to run the Library Management System.
    """
    storage = Storage()

    # Authenticate manager login
    if not login():
        return

    while True:
        # Display menu options
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Add a User")
        print("7. List Users")
        print("8. Search Users")
        print("9. Update User")
        print("10. Delete User")
        print("11. Check-in a Book")
        print("12. Check-out a Book")
        print("13. Exit")

        try:
            choice = input("Enter choice: ")

            if choice == '1':
                # Add a Book
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                books_available = int(input("Enter number of copies available: "))
                storage.add_book(title, author, isbn, books_available)
                print(f'{title} book is added')

            elif choice == '2':
                # List Books
                books = storage.list_books()
                print("\nBooks:")
                for book in books:
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.books_available}")

            elif choice == '3':
                # Search Books
                keyword = input("Enter search keyword: ")
                by = input("Search by (title/author/isbn): ")
                books = storage.search_books(keyword, by)
                print("\nSearch Results:")
                for book in books:
                    print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.books_available}")

            elif choice == '4':
                # Update Book
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                books_available = input("Enter new number of copies available (leave blank to keep current): ")
                storage.update_book(isbn, title, author, int(books_available) if books_available else None)

            elif choice == '5':
                # Delete Book
                isbn = input("Enter ISBN of the book to delete: ")
                storage.delete_book(isbn)
                print(f'Book with ISBN {isbn} deleted.')

            elif choice == '6':
                # Add User
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                mobile_num = input("Enter mobile number (optional): ")
                storage.add_user(name, user_id, mobile_num)

            elif choice == '7':
                # List Users
                users = storage.list_users()
                print("\nUsers:")
                for user in users:
                    print(f"Name: {user.name}, User ID: {user.user_id}, Mobile: {user.mobile_num}")

            elif choice == '8':
                # Search Users
                keyword = input("Enter search keyword: ")
                by = input("Search by (name/user_id): ")
                users = storage.search_users(keyword, by)
                print("\nSearch Results:")
                for user in users:
                    print(f"Name: {user.name}, User ID: {user.user_id}, Mobile: {user.mobile_num}")

            elif choice == '9':
                # Update User
                user_id = input("Enter user ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                storage.update_user(user_id, name)

            elif choice == '10':
                # Delete User
                user_id = input("Enter user ID to delete: ")
                storage.delete_user(user_id)
                print(f'User with ID {user_id} deleted.')

            elif choice == '11':
                # Check-in a Book
                user_id = input("Enter User ID: ")
                user_name = input("Enter User Name: ")
                book_isbn = input("Enter book ISBN: ")
                book_title = input("Enter book title: ")
                storage.log_book_check_in(user_id, user_name, book_isbn, book_title)

            elif choice == '12':
                # Check-out a Book
                in_out_id = input("Enter In/Out ID: ")
                storage.log_book_check_out(in_out_id)

            elif choice == '13':
                # Exit the program
                print("Exiting Library Management System.")
                sys.exit()

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
