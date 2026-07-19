class Book:
    """Represents a book stored in the library."""

    total_books = 0

    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = self._validate_text(title, "Book title")
        self.author = self._validate_text(author, "Author name")
        self.isbn = self._validate_text(isbn, "ISBN")
        self.__available = True
        Book.total_books += 1

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty.")
        return value

    @property
    def available(self) -> bool:
        """Get the current availability status."""
        return self.__available

    @available.setter
    def available(self, value: bool) -> None:
        """Allow availability to be changed only with a Boolean value."""
        if not isinstance(value, bool):
            raise TypeError("Availability must be True or False.")
        self.__available = value

    @property
    def status(self) -> str:
        """Read-only human-readable availability status."""
        return "Available" if self.available else "Borrowed"

    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books

    def display_book(self) -> None:
        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {self.status}")
