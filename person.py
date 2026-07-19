class Person:
    """Parent class for people associated with the library."""

    def __init__(self, name: str, age: int) -> None:
        self.name = self.validate_non_empty(name, "Name")
        self.age = age

    @staticmethod
    def validate_non_empty(value: str, field_name: str) -> str:
        """Validate and return a non-empty string."""
        value = value.strip()
        if not value:
            raise ValueError(f"{field_name} cannot be empty.")
        return value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Age must be greater than 0.")
        self._age = value

    def display_info(self) -> None:
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
