# Library unittest
import unittest
from library.book import Book
from library.user import User
from library.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Set up test book and users
        self.library = Library()
        self.book1 = Book(title="Test 1", author="Author 1", isbn="1234")
        self.user1 = User(name="Mike", user_id="001")
        self.user2 = User(name="Bobby", user_id="003")

        # Add books and users to the library
        self.library.add_book(self.book1)
        self.library.add_user(self.user1)
        self.library.add_user(self.user2)

    def test_add_book(self):
        # Add book to library and confirm addition
        print("\nTest add_book (library.py)")
        book_addition = Book("Book 2", "Test Author", "4321")
        self.library.add_book(book_addition)
        self.assertIn(book_addition, self.library.books)

    def test_remove_book(self):
        # Check for book1, remove book1, and confirm deletion
        print("\nTest remove_book (library.py)")
        self.assertIn(self.book1, self.library.books)
        self.library.remove_book("1234")
        self.assertNotIn(self.book1, self.library.books)

    def test_add_user(self):
        # Add new user and confirm addition
        print("\nTest add_user (library.py)")
        new_user = User("John", "002")
        self.library.add_user(new_user)
        self.assertIn(self.user1, self.library.users)

    def test_remove_user(self):
        # Remove user and confirm removal
        print("\nTest remove_user (library.py)")
        self.library.remove_user("003")
        self.assertNotIn(self.user2, self.library.users)

    def test_borrow_book(self):
        # Test borrow_book, confirm in borrowed_books,
        # and confirm marked not available
        print("\nTest borrow_book (library.py)")
        result = self.library.borrow_book(self.user1, "1234")
        self.assertTrue(result)
        self.assertTrue(self.user1.borrowed_books)
        self.assertFalse(self.book1.available)

    def test_return_book(self):
        # Test return_book, confirm marked available, and not
        # in borrowed_books
        print("\nTest return_book (library.py)")
        self.library.borrow_book(self.user1, "1234")
        result = self.library.return_book(self.user1.name, "1234")
        self.assertTrue(result)
        self.assertTrue(self.book1.available)
        self.assertNotIn(self.book1, self.user1.borrowed_books)


if __name__ == "__main__":
    unittest.main()
