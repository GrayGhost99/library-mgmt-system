# Library class

import csv


class Library:
    def __init__(self):
        self.books = []
        self.users = []


    def add_book(self, book):
        self.books.append(book)


    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]


    def add_user(self, user):
        self.users.append(user)


    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]


    def borrow_book(self, user, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                return user.borrow_book(book)
        return False


    def return_book(self, user, isbn):
        for book in user.borrowed_books:
            if book.isbn == isbn:
                return user.return_book(book)
        return False


    def list_available_books(self):
        return [str(book) for book in self.books if book.available]
