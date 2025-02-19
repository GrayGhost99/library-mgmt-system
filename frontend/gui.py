# Tkinter frontend
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from library.library import Library
from library.book import Book
from library.user import User


class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")

        self.label = tk.Label(root, text="Library Management System", font=("Arial", 16))
        self.label.pack()

        # User Input Fields
        self.user_label = tk.Label(root, text="User Name:")
        self.user_label.pack()
        self.user_entry = tk.Entry(root)
        self.user_entry.pack()

        self.user_id_label = tk.Label(root, text="User ID:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()
        
        # Book Input Fields
        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()
        
        self.isbn_label = tk.Label(root, text="ISBN:")
        self.isbn_label.pack()
        self.isbn_entry = tk.Entry(root)
        self.isbn_entry.pack()

        # Add User Button
        self.add_user_button = tk.Button(root, text="Add User", command=self.add_user)
        self.add_user_button.pack()
        
        # Remove User Button
        self.remove_user_button = tk.Button(root, text="Remove User", command=self.remove_user)
        self.remove_user_button.pack()
        
        # Add Book Button
        self.add_book_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_book_button.pack()
        

        # Listbox to Show Books
        self.book_listbox = tk.Listbox(root, width=80)
        self.book_listbox.pack()
        
        # List Users Button
        self.remove_user_button = tk.Button(root, text="List Users", command=self.update_user_list)
        self.remove_user_button.pack()

        # Buttons for Managing Books
        self.remove_book_button = tk.Button(root, text="Remove Book")                                               # ADD LOGIC FOR REMOVE BOOK
        self.remove_book_button.pack()

        self.borrow_book_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.borrow_book_button.pack()

        self.return_book_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_book_button.pack()
        
        self.borrowed_book_button = tk.Button(root, text="List Borrowed Books", command=self.list_borrowed_books)
        self.borrowed_book_button.pack()
        
        self.list_book_button = tk.Button(root, text="List Available Books", command=self.list_available_books)
        self.list_book_button.pack()

        self.update_book_list()

    def add_user(self):
        name = self.user_entry.get().strip()
        user_id = self.user_id_entry.get().strip()
        
        if name and user_id:
            user = User(name, user_id)
            self.library.add_user(user)
            print(f"Added user: {user.name} (ID: {user.user_id})")  # Debugging output
            self.update_user_list()

            
    def remove_user(self):
        # Remove a user
        name = self.user_entry.get().strip()
        user_id = self.user_id_entry.get().strip()

        if name and user_id:
            self.library.remove_user(user_id)
            messagebox.showinfo("Success", f"User {name} (ID: {user_id}) removed!")
            self.user_entry.delete(0, tk.END)
            self.user_id_entry.delete(0, tk.END)
            self.update_user_list()
        else:
            messagebox.showwarning("Warning", "Please enter both Name and User ID.")
    
    def update_user_list(self):
        self.book_listbox.delete(0, tk.END)
        for user in self.library.list_users():
            self.book_listbox.insert(tk.END, f"{user.name} (ID: {user.user_id})")

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        isbn = self.isbn_entry.get().strip()
        book = Book(title, author, isbn)
        self.library.add_book(book)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.update_book_list()

    def borrow_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            book_info = self.book_listbox.get(selected_index[0])
            isbn = book_info.split("(ISBN: ")[1].split(")")[0]
            user = User(str(self.user_entry.get().strip()), str(self.user_id_entry.get().strip()))                                          
            if self.library.borrow_book(user, isbn):
                messagebox.showinfo("Success", f"{user.name} borrowed {book_info}")
                self.update_book_list()
            else:
                messagebox.showwarning("Warning", "Book not available")

    def return_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            book_info = self.book_listbox.get(selected_index[0])
            isbn = book_info.split("(ISBN: ")[1].split(")")[0]
            user_name = self.user_entry.get().strip()


            if self.library.return_book(user_name, isbn):
                messagebox.showinfo("Success", f"{user_name} returned {book_info}")
                self.update_book_list()
            else:
                messagebox.showwarning("Error", f"Could not return book for {user_name}")

    def update_book_list(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.library.list_available_books():
            self.book_listbox.insert(tk.END, book)
            
    def list_borrowed_books(self):
        self.book_listbox.delete(0, tk.END)
        for user in self.library.list_borrowed_books():
            self.book_listbox.insert(tk.END, str(user))
            
    def list_available_books(self):
        self.book_listbox.delete(0, tk.END)
        for user in self.library.list_available_books():
            self.book_listbox.insert(tk.END, str(user))

if __name__ == "__main__":
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()

