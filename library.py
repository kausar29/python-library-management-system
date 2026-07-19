from book import Book
from member import Member


class Library:
    """Contains and manages Book and Member objects (composition)."""

    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_book(self, title: str, author: str, isbn: str) -> Book:
        if self.find_book_by_isbn(isbn) is not None:
            raise ValueError("ISBN already exists.")

        book = Book(title, author, isbn)
        self.books.append(book)
        return book

    def register_member(self, member_id: str, name: str, age: int) -> Member:
        if self.find_member(member_id) is not None:
            raise ValueError("Member ID already exists.")

        member = Member(member_id, name, age)
        self.members.append(member)
        return member

    def borrow_book(self, member_id: str, isbn: str) -> str:
        member = self.find_member(member_id)
        if member is None:
            return "Member not found."

        book = self.find_book_by_isbn(isbn)
        if book is None:
            return "Book not found."

        if not book.available:
            return "Sorry! This book is currently unavailable."

        member.borrow_book(book)
        book.available = False
        return "Book borrowed successfully."

    def return_book(self, member_id: str, isbn: str) -> str:
        member = self.find_member(member_id)
        if member is None:
            return "Member not found."

        book = self.find_book_by_isbn(isbn)
        if book is None:
            return "Book not found."

        if book not in member.borrowed_books:
            return "This member did not borrow this book."

        member.return_book(book)
        book.available = True
        return "Book returned successfully."

    def show_books(self) -> None:
        print("------------- BOOK LIST -------------")
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:
            book.display_book()
            print("-------------------------------------")

    def show_members(self) -> None:
        print("----------- MEMBER LIST ------------")
        if not self.members:
            print("No members registered.")
            return

        for member in self.members:
            member.display_info()
            print("------------------------------------")

    def search_book(self, title: str) -> list[Book]:
        search_text = title.strip().lower()
        if not search_text:
            raise ValueError("Book title cannot be empty.")

        return [book for book in self.books if search_text in book.title.lower()]

    def find_book_by_isbn(self, isbn: str) -> Book | None:
        isbn = isbn.strip().lower()
        return next((book for book in self.books if book.isbn.lower() == isbn), None)

    def find_member(self, member_id: str) -> Member | None:
        member_id = member_id.strip().lower()
        return next(
            (member for member in self.members if member.member_id.lower() == member_id),
            None,
        )
