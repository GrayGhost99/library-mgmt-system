# User unittest
import unittest
from library.user import User
from library.book import Book


class TestUser(unittest.TestCase):
    def test_init_user(self):
        # Test user class init
        print("\nTest user initialization (test_user.py)")
        user = User(name="Michael", user_id="001")
        self.assertEqual(user.name, "Michael")
        self.assertEqual(user.user_id, "001")

    def setUp(self):
        # Set up a user and book
        self.user = User(name="Michael", user_id="001")
        self.book = Book(title="My Book", author="Michael", isbn="123")

    def test_borrow_book(self):
        # Borrow book, confirm borrowed, confirm in users list of books
        # and confirm book unavailable
        print("\nTest borrow_book (test_user.py)")
        result = self.user.borrow_book(self.book)
        self.assertTrue(result)
        self.assertIn(self.book, self.user.borrowed_books)
        self.assertFalse(self.book.available)

    def test_return_book(self):
        # Borrow book, return book, make sure not in users borrowed books
        # and make sure its in the available books
        print("\nTest return_book (test_user.py)")
        self.user.borrow_book(self.book)
        result = self.user.return_book(self.book)
        self.assertTrue(result)
        self.assertNotIn(self.book, self.user.borrowed_books)
        self.assertTrue(self.book.available)

    def test_view_borrowed(self):
        print("\nTest view borrowed books (test_user.py)")
        self.user.borrow_book(self.book)
        borrowed_books = self.user.view_borrowed_books()
        self.assertEqual(len(borrowed_books), 1)
        self.assertIn(
            f"{self.book.title} by {self.book.author} (ISBN: {self.book.isbn}) - Borrowed",  # (ISBN: 123)
            borrowed_books,
        )
