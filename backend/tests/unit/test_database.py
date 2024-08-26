from enum import auto
from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, Title, Description, ISBN 

from src.infrastructure.database.repository import FakeAuthorRepository, FakeBookRepository


def create_author() -> Author:
    fullname = FullName(first_name="John", last_name="Doe")
    author = Author(fullname=fullname, biography="A famous author")

    return author


def test_create_author(session) -> None:
    author = create_author()

    session.add(author)
    session.commit()

    retrieved_author = session.query(Author).first()

    assert retrieved_author is not None
    assert retrieved_author.fullname.first_name == "John"
    assert retrieved_author.fullname.last_name == "Doe"
    assert retrieved_author.biography == "A famous author"


def test_create_book(session) -> None:
    author = create_author()
    title = Title(value="A Great Book")
    description = Description(value="An interesting description")
    isbn = ISBN(value="123-456-789")
    book = Book(title=title, description=description, author=author, isbn=isbn)

    session.add(author)
    session.add(book)
    session.commit()
    retrieved_book = session.query(Book).first()

    assert retrieved_book is not None
    assert retrieved_book.title.value == "A Great Book"
    assert retrieved_book.description.value == "An interesting description"
    assert retrieved_book.isbn.value == "123-456-789"
    assert retrieved_book.author.fullname.first_name == "John"
    assert retrieved_book.author.fullname.last_name == "Doe"


def test_repository_can_create_a_author() -> None:
    author = create_author()
    repository = FakeAuthorRepository()

    repository.create(instance=author)
    retrieved_author = repository.get(key="id", value=author.id)

    assert retrieved_author is not None
    assert retrieved_author.id == author.id
    assert retrieved_author.fullname.first_name == author.fullname.first_name
    assert retrieved_author.fullname.last_name == author.fullname.last_name
    assert retrieved_author.biography == author.biography


def test_repository_can_create_a_book() -> None:
    author = create_author()
    title = Title(value="A Great Book")
    description = Description(value="An interesting description")
    isbn = ISBN(value="123-456-789")
    book = Book(title=title, description=description, author=author, isbn=isbn)
    repository = FakeBookRepository()

    repository.create(instance=book)
    retrieved_book = repository.get(key="id", value=book.id)

    assert retrieved_book is not None
    assert retrieved_book.title == book.title
    assert retrieved_book.description.value == book.description.value
    assert retrieved_book.isbn.value == book.value
    assert retrieved_book.author.fullname.first_name == book.author.fullname.first_name
    assert retrieved_book.author.fullname.last_name == book.author.fullname.last_name
    
