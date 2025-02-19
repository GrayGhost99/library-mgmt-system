# Library class

from library.user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []


    def add_book(self, book):
        self.books.append(book)


    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]


    def add_user(self, user):
        user.name = user.name.strip().lower()  
        self.users.append(user)


    def list_users(self):
        return self.users  


    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]


    def borrow_book(self, user_name, isbn):
        # Ensure `user_name` is a string
        if isinstance(user_name, User):  
            user_name = user_name.name  

        # Find the user
        user = next((u for u in self.users if u.name.strip().lower() == user_name.strip().lower()), None)
        if not user:
            return False

        # Find the book
        book = next((b for b in self.books if b.isbn == isbn and b.available), None)
        if not book:
            return False

        # Borrow the book
        return user.borrow_book(book)

    def return_book(self, user_name, isbn):
        # Find the user
        user = next((u for u in self.users if u.name == user_name), None)
        if not user:
            return False

        # Find the book in the user's borrowed books
        for book in user.borrowed_books:
            if book.isbn == isbn:
                return user.return_book(book)

        return False


    def list_available_books(self):
        return [str(book) for book in self.books if book.available]
    
    def list_borrowed_books(self):
        return [str(book) for book in self.books if book.available != True] 
