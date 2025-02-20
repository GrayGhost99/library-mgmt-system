import unittest
from library.book import Book


class TestBook(unittest.TestCase):
    def test_init_book(self):
        # Test book class init
        print("\nTest book initialization (test_book.py)")
        book = Book(title="My New Book", author="Michael", isbn="1234")
        self.assertEqual(book.title, "My New Book")
        self.assertEqual(book.author, "Michael")
        self.assertEqual(book.isbn, "1234")
        self.assertTrue(book.available)

    def test_borrow_book(self):
        # Create an instance of the Book class
        print("\nTest borrow_book (test_book.py)")
        book = Book(title="My New Book", author="Michael", isbn="1234")

        # Test that book is available, borrow book
        # then check that it is not available
        self.assertTrue(book.available)
        book.borrow_book()
        self.assertFalse(book.available)

    def test_return_book(self):
        # Create an instance of the Book class
        print("\nTest return_book (test_book.py)")
        book = Book(title="My New Book", author="Michael", isbn="1234")

        # Borrow book, check that it is unavailable
        # return book, check that it is available
        # attempt to return a second time - should be False
        book.borrow_book()
        self.assertFalse(book.available)
        book.return_book()
        self.assertTrue(book.available)
        result = book.return_book()
        self.assertFalse(result)

    def test_str_representation(self):
        print("\nTest string representation of a book (test_book.py)")
        book = Book("My Test Book", "Michael", 1234)
        returned_str = "My Test Book by Michael (ISBN: 1234) - Available"
        self.assertEqual(str(book), returned_str)
