# Tkinter frontend

import tkinter as tk
from tkinter import messagebox
from library.library import Library
from library.book import Book
from library.user import User

# add input fields and redirect button for 'Add Books'
# add button for 'Remove Book' and 'Add Book' and add logic for same
# add button for 'Remove Book' and write logic for remove / update logic for Add Book / move these buttons and create 3 new boxes for title, author, isbn
# add 'List Books' button - this should be only button that interacts with list box
# additional : add a 'View Borrowed Books' button to clear list box and list borrowed books by user


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

        # Add User Button
        self.add_user_button = tk.Button(root, text="Add User", command=self.add_user)
        self.add_user_button.pack()

        # Listbox to Show Books
        self.book_listbox = tk.Listbox(root, width=80)
        self.book_listbox.pack()

        # Buttons for Managing Books
        self.add_book_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_book_button.pack()

        self.borrow_book_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.borrow_book_button.pack()

        self.return_book_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_book_button.pack()

        self.update_book_list()

    def add_user(self):
        """Create a new user and add to the library."""
        name = self.user_entry.get().strip()
        user_id = self.user_id_entry.get().strip()
        
        if name and user_id:
            user = User(name, user_id)
            self.library.add_user(user)
            messagebox.showinfo("Success", f"User {name} (ID: {user_id}) added!")
            self.user_entry.delete(0, tk.END)
            self.user_id_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both Name and User ID.")

    def add_book(self):
        book = Book("Sample Book", "Sample Author", "123456")
        self.library.add_book(book)
        self.update_book_list()

    def borrow_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            book_info = self.book_listbox.get(selected_index[0])
            isbn = book_info.split("(ISBN: ")[1].split(")")[0]
            user = User("Sample User", "U001")
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
            user = User("Sample User", "U001")
            if self.library.return_book(user, isbn):
                messagebox.showinfo("Success", f"{user.name} returned {book_info}")
                self.update_book_list()

    def update_book_list(self):
        self.book_listbox.delete(0, tk.END)
        for book in self.library.list_available_books():
            self.book_listbox.insert(tk.END, book)

if __name__ == "__main__":
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()

