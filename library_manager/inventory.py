import json
from .book import Book
from pathlib import Path
import logging

class LibraryInventory:
    def __init__(self, filename = "book.json"):
        self.filename = Path(filename)
        self.books = self.load_books()
    
    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Added book: {book.title}")
        self.save_books()
    
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_all(self):
        if not self.books:
            print("The Library is empty.")
            return
        for book in self.books:
            print(book)

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
            logging.info("Books saved successfully.")
        except IOError as e:
            logging.error(f"Error saving books: {e}")
    
    def load_books(self):
        if not self.filename.exists():
            logging.warning("Book file not found. Starting with an empty inventory.")
            return []
        
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                books = [Book(**data) for data in books_data]
            logging.info("Books loaded successfully.")
            return books
        except (json.JSONDecodedError, IOError) as e:
            logging.error(f"Error loading books: {e}")
            return []