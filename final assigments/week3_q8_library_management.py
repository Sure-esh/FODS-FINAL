'''
Library Management System
Features: Borrow book, Return book, Search book
Uses OOP concepts, file handling, and exception handling
'''

import os
import csv
from datetime import datetime

# Define Book class
class Book:
    def __init__(self, book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available
    
    def display(self):
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {self.copies_available}")

# Define Library class
class Library:
    def __init__(self, filename="books.csv", borrow_file="borrowed.csv"):
        self.filename = filename
        self.borrow_file = borrow_file
        self.books = {}
        self.load_books()
    
    # Load books from file
    def load_books(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['book_id']:
                            book = Book(row['book_id'], row['title'], row['author'], int(row['copies_available']))
                            self.books[row['book_id']] = book
        except Exception as e:
            print(f"Error loading books: {e}")
    
    # Save books to file
    def save_books(self):
        try:
            with open(self.filename, 'w', newline='') as file:
                fieldnames = ['book_id', 'title', 'author', 'copies_available']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book_id, book in self.books.items():
                    writer.writerow({
                        'book_id': book.book_id,
                        'title': book.title,
                        'author': book.author,
                        'copies_available': book.copies_available
                    })
        except Exception as e:
            print(f"Error saving books: {e}")
    
    # Initialize borrow file
    def init_borrow_file(self):
        if not os.path.exists(self.borrow_file):
            with open(self.borrow_file, 'w', newline='') as file:
                fieldnames = ['member_name', 'book_id', 'book_title', 'borrow_date', 'return_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
    
    # Borrow book
    def borrow_book(self, member_name, book_id):
        self.init_borrow_file()
        
        try:
            if book_id not in self.books:
                print(f"Error: Book with ID {book_id} not found!")
                return
            
            book = self.books[book_id]
            
            if book.copies_available <= 0:
                print(f"Error: '{book.title}' is not available!")
                return
            
            # Reduce available copies
            book.copies_available -= 1
            
            # Record borrow
            with open(self.borrow_file, 'a', newline='') as file:
                fieldnames = ['member_name', 'book_id', 'book_title', 'borrow_date', 'return_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({
                    'member_name': member_name,
                    'book_id': book_id,
                    'book_title': book.title,
                    'borrow_date': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'return_date': ''
                })
            
            self.save_books()
            print(f"✓ You have borrowed '{book.title}'")
        
        except Exception as e:
            print(f"Error borrowing book: {e}")
    
    # Return book
    def return_book(self, member_name, book_id):
        try:
            if book_id not in self.books:
                print(f"Error: Book with ID {book_id} not found!")
                return
            
            book = self.books[book_id]
            book.copies_available += 1
            
            # Update borrow record
            temp_data = []
            with open(self.borrow_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['member_name'] == member_name and row['book_id'] == book_id and row['return_date'] == '':
                        row['return_date'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    temp_data.append(row)
            
            with open(self.borrow_file, 'w', newline='') as file:
                fieldnames = ['member_name', 'book_id', 'book_title', 'borrow_date', 'return_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(temp_data)
            
            self.save_books()
            print(f"✓ You have returned '{book.title}'")
        
        except Exception as e:
            print(f"Error returning book: {e}")
    
    # Search book
    def search_book(self, query):
        try:
            print("\n" + "="*70)
            print("SEARCH RESULTS")
            print("="*70)
            
            found = False
            for book_id, book in self.books.items():
                if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                    book.display()
                    found = True
            
            if not found:
                print("No books found!")
            
            print("="*70)
        except Exception as e:
            print(f"Error searching: {e}")
    
    # Display all books
    def display_all_books(self):
        try:
            print("\n" + "="*70)
            print("LIBRARY BOOKS")
            print("="*70)
            
            if not self.books:
                print("No books in library!")
            else:
                for book_id, book in self.books.items():
                    book.display()
            
            print("="*70)
        except Exception as e:
            print(f"Error displaying books: {e}")

# Main program
if __name__ == "__main__":
    library = Library()
    
    # Add some sample books if file is empty
    if not library.books:
        sample_books = [
            Book("1132", "Python", "Suresh Dhital", 3),
            Book("3344", "C++", "Nishant Dhital", 3),
            Book("1223", "Rust", "Anusha Timilsina", 3),
            Book("423", "Art of Hacking", "Jenish Dhital", 3)
        ]
        
        for book in sample_books:
            library.books[book.book_id] = book
        
        library.save_books()
        print("✓ Books loaded to library")
    
    # Menu loop
    while True:
        print("\n" + "="*50)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Search book")
        print("4. View all books")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            member = input("Enter your name: ").strip()
            book_id = input("Enter book ID: ").strip()
            library.borrow_book(member, book_id)
        
        elif choice == '2':
            member = input("Enter your name: ").strip()
            book_id = input("Enter book ID: ").strip()
            library.return_book(member, book_id)
        
        elif choice == '3':
            query = input("Enter book title or author name to search: ").strip()
            library.search_book(query)
        
        elif choice == '4':
            library.display_all_books()
        
        elif choice == '5':
            print("Thank you for using Library Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")
