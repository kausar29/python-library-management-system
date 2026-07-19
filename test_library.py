import unittest

from library import Library


class LibraryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library()
        self.library.add_book("Python Programming", "John Smith", "B101")
        self.library.register_member("M001", "Naimur", 23)

    def test_borrow_and_return_book(self) -> None:
        self.assertEqual(
            self.library.borrow_book("M001", "B101"),
            "Book borrowed successfully.",
        )
        self.assertFalse(self.library.books[0].available)

        self.assertEqual(
            self.library.return_book("M001", "B101"),
            "Book returned successfully.",
        )
        self.assertTrue(self.library.books[0].available)

    def test_duplicate_isbn(self) -> None:
        with self.assertRaisesRegex(ValueError, "ISBN already exists"):
            self.library.add_book("Another Book", "Another Author", "B101")

    def test_invalid_age(self) -> None:
        with self.assertRaisesRegex(ValueError, "Age must be greater than 0"):
            self.library.register_member("M002", "Sara", -5)

    def test_search_book_case_insensitive(self) -> None:
        results = self.library.search_book("python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].isbn, "B101")


if __name__ == "__main__":
    unittest.main()
