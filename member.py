from person import Person
from book import Book


class Member(Person):
    """A registered library member; inherits from Person."""

    total_members = 0

    def __init__(self, member_id: str, name: str, age: int) -> None:
        super().__init__(name, age)
        self.member_id = self.validate_non_empty(member_id, "Member ID")
        self.borrowed_books: list[Book] = []
        Member.total_members += 1

    def borrow_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            raise ValueError("A member cannot borrow the same book twice.")
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        if book not in self.borrowed_books:
            raise ValueError("This member did not borrow this book.")
        self.borrowed_books.remove(book)

    @classmethod
    def get_total_members(cls) -> int:
        return cls.total_members

    def display_info(self) -> None:
        """Override Person.display_info()."""
        print(f"Member ID : {self.member_id}")
        super().display_info()
        print(f"Borrowed Books : {len(self.borrowed_books)}")
