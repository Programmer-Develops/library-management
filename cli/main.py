from library_manager.book import Book
from library_manager.inventory import LibraryInventory
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main_menu():
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add a new book")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. Search for a book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            inventory.add_book(new_book)
            print("Book added.")
        
        elif choice == '2':
            isbn = input("Enter ISBN of the book to issue: ")
            found_books = inventory.search_by_isbn(isbn)
            print(f"Search result: {found_books}")
            if found_books and found_books[0].issue():
                print("Book issued successfully.")
            else:
                print("Book not found or is not available.")
            inventory.save_books()
        
        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            found_books = inventory.search_by_isbn(isbn)
            if found_books and found_books[0].return_book():
                print("Book returned successfully.")
            else:
                print("Book not found or is already available.")
            inventory.save_books()
        
        elif choice == '4':
            inventory.display_all()
        
        elif choice == '5':
            query = input("Enter title or ISBN to search: ")
            results = inventory.search_by_title(query) or inventory.search_by_isbn(query)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")
        
        elif choice == '6':
            print("Exiting.")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()