from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, Title, Description, ISBN 


def test_create_author(session):
    fullname = FullName(first_name="John", last_name="Doe")
    author = Author(fullname=fullname, biography="A famous author")

    session.add(author)
    session.commit()

    retrieved_author = session.query(Author).first()

    assert retrieved_author is not None
    assert retrieved_author.fullname.first_name == "John"
    assert retrieved_author.fullname.last_name == "Doe"
    assert retrieved_author.biography == "A famous author"


def test_create_book(session):
    fullname = FullName(first_name="John", last_name="Doe")
    author = Author(fullname=fullname, biography="A famous author")
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

