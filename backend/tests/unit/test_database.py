from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, Title, Description, ISBN 

from .common.fake_repository import FakeAuthorRepository, FakeBookRepository


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
    title = Title(value="A Great Book")
    description = Description(value="An interesting description")
    isbn = ISBN(value="12324561789")
    book = Book(title=title, description=description, isbn=isbn)

    session.add(book)
    session.commit()

    retrieved_book = session.query(Book).first()
    assert retrieved_book is not None
    assert retrieved_book.title.value == "A Great Book"
    assert retrieved_book.description.value == "An interesting description"
    assert retrieved_book.isbn.value == "12324561789"
    assert len(retrieved_book.authors) == 0


def test_create_book_with_two_authors(session) -> None:
    author1 = Author(fullname=FullName(first_name="John", last_name="Doe"))
    author2 = Author(fullname=FullName(first_name="Jane", last_name="Smith"))

    title = Title(value="A Great Book")
    description = Description(value="An interesting description")
    isbn = ISBN(value="12324561789")
    book = Book(title=title, description=description, isbn=isbn)
    
    book.add_author(author1)
    book.add_author(author2)

    session.add(book)
    session.add(author1)
    session.add(author2)
    session.commit()

    retrieved_book = session.query(Book).first()
    assert retrieved_book is not None
    assert retrieved_book.title.value == "A Great Book"
    assert retrieved_book.description.value == "An interesting description"
    assert retrieved_book.isbn.value == "12324561789"
    assert len(retrieved_book.authors) == 2

    assert retrieved_book.authors == set([author1, author2])
