# User class

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    
    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"
    
    
    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False
    
    
    def return_book(self, book):
        if self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False
    
    
    def view_borrowed_books(self):
        return[str(book) for book in self.borrowed_books]