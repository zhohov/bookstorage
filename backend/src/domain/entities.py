import uuid
from typing import Optional, Set

from .value_objects import ISBN, FullName, Title, Description


class BaseEntity:
    def __init__(self) -> None:
        self.id = uuid.uuid4()

    def __hash__(self) -> int:
        return hash(self.id)


class Author(BaseEntity):
    def __init__(
        self, fullname: FullName, biography: Optional[str] = None
    )-> None:
        super().__init__()
        self.fullname = fullname
        self.biography = biography
        self.books: Set["Book"] = set()

    def update_biography(self, biography: str) -> None:
        self.biography = biography

    def add_book(self, book: "Book") -> None:
        self.books.add(book)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Author):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return super().__hash__()


class Book(BaseEntity):
    def __init__(
        self, title: Title, description: Description, isbn: ISBN, filename: Optional[str] = None, 
    ) -> None:
        super().__init__()
        self.title = title
        self.description = description
        self.authors: Set[Author] = set()
        self.isbn = isbn
        self.is_available: bool = False
        self.filename = filename

    def update_availability(self, value: bool) -> None:
        self.is_available = value

    def update_filename(self, value: str) -> None:
        self.filename = value

    def add_author(self, author: Author) -> None:
        self.authors.add(author)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return super().__hash__()

