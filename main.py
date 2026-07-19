import os
from library import Library


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    input("\nPress Enter to continue...")


def get_required_input(prompt: str, field_name: str) -> str:
    value = input(prompt).strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value


def show_menu() -> None:
    print("=" * 41)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 41)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Search Book")
    print("8. Exit")


def add_book_ui(library: Library) -> None:
    print("----- Add New Book -----")
    title = get_required_input("Enter Book Title : ", "Book title")
    author = get_required_input("Enter Author : ", "Author name")
    isbn = get_required_input("Enter ISBN : ", "ISBN")
    library.add_book(title, author, isbn)
    print("Book added successfully!")


def register_member_ui(library: Library) -> None:
    print("----- Register Member -----")
    member_id = get_required_input("Enter Member ID : ", "Member ID")
    name = get_required_input("Enter Name : ", "Name")
    age_text = get_required_input("Enter Age : ", "Age")

    try:
        age = int(age_text)
    except ValueError as exc:
        raise ValueError("Age must be a valid integer.") from exc

    library.register_member(member_id, name, age)
    print("Member registered successfully!")


def borrow_book_ui(library: Library) -> None:
    print("------ Borrow Book ------")
    member_id = get_required_input("Enter Member ID : ", "Member ID")
    isbn = get_required_input("Enter Book ISBN : ", "ISBN")
    print(library.borrow_book(member_id, isbn))


def return_book_ui(library: Library) -> None:
    print("------ Return Book ------")
    member_id = get_required_input("Enter Member ID : ", "Member ID")
    isbn = get_required_input("Enter Book ISBN : ", "ISBN")
    print(library.return_book(member_id, isbn))


def search_book_ui(library: Library) -> None:
    print("------ Search Book ------")
    title = get_required_input("Enter Book Title : ", "Book title")
    matches = library.search_book(title)

    if not matches:
        print("Book not found.")
        return

    for index, book in enumerate(matches):
        print("Book Found!")
        book.display_book()
        if index < len(matches) - 1:
            print("-------------------------------------")


def main() -> None:
    library = Library()

    actions = {
        1: lambda: add_book_ui(library),
        2: lambda: register_member_ui(library),
        3: lambda: borrow_book_ui(library),
        4: lambda: return_book_ui(library),
        5: library.show_books,
        6: library.show_members,
        7: lambda: search_book_ui(library),
    }

    while True:
        clear_screen()
        show_menu()

        try:
            choice = int(input("Enter your choice: ").strip())

            if choice == 8:
                print("Thank you for using Library Management System.")
                print("Goodbye!")
                break

            action = actions.get(choice)
            if action is None:
                raise ValueError("Invalid menu choice. Please enter a number from 1 to 8.")

            action()

        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as error:
            print(f"Unexpected error: {error}")

        pause()


if __name__ == "__main__":
    main()
