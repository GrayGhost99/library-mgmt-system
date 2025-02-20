# Book class


class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        # return string representation of book
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Borrowed'}"

    def borrow_book(self):
        # borrow book - if available set to False / return True - if not available return False
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        # return book - if not showing available sets to available (True) returns True
        # otherwise returns False (wasn't needed)
        if not self.available:
            self.available = True
            return True
        return False
