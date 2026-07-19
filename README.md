# Python Library Management System

A console-based Library Management System developed with Python Object-Oriented Programming.

## OOP concepts used

- Classes and objects
- Constructors (`__init__`)
- Inheritance (`Member` inherits from `Person`)
- Method overriding (`Member.display_info`)
- Encapsulation (`Book.__available`)
- Getter/setter with `@property`
- Read-only property (`Book.status`)
- Class variables and class methods
- Static methods
- Composition (`Library` contains books and members)
- Exception handling and input validation

## Project files

- `main.py` - menu and program entry point
- `person.py` - parent `Person` class
- `member.py` - child `Member` class
- `book.py` - `Book` class
- `library.py` - `Library` class and management logic

## Run the project

```bash
python main.py
```

No external package or database is required. All data remains in memory and is cleared when the program exits.
