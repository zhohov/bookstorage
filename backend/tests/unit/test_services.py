from typing import List

from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, Title, Description, ISBN
from src.application.services.services import AuthorService, BookService

from src.application.dto.dto import AuthorInput, AuthorOutput, BookInput, BookOutput

from .common.fake_uow import FakeUnitOfWork


def test_create_author() -> None:
    uow = FakeUnitOfWork()
    service = AuthorService(uow=uow)
    fullname = FullName(first_name="John", last_name="Doe")
    payload = AuthorInput(fullname=fullname, biography="A famous author")

    author = service.create(payload=payload)
    retrieved_author = service.get(key="id", value=author.id)

    assert isinstance(author, Author)
    assert retrieved_author.id == author.id
    assert retrieved_author.fullname["first_name"] == author.fullname.first_name


def test_get_all_authors() -> None:
    uow = FakeUnitOfWork()
    service = AuthorService(uow=uow)
    fullname = FullName(first_name="John", last_name="Doe")
    payload = AuthorInput(fullname=fullname, biography="A famous author")

    author = service.create(payload=payload)
    retrieved_authors = service.all()

    expected = [AuthorOutput(**author.to_dict())]

    assert isinstance(retrieved_authors, List)
    assert retrieved_authors == expected


class TestBookService:
    def test_create_book(self, ) -> None:
        uow = FakeUnitOfWork()
        service = BookService(uow=uow)
        title = Title(value="Domain-Driven Design: Tackling Complexity in the Heart of Software")
        description = Description(value="Book about Domain-Driven Design")
        isbn = ISBN(value="9780321125217")
        payload = BookInput(title=title, description=description, isbn=isbn)

        book = service.create(payload=payload)
        retrieved_book = service.get(key="id", value=book.id)

        assert isinstance(book, Book)
        assert isinstance(retrieved_book, BookOutput)
        assert retrieved_book.title == book.title
        assert retrieved_book.description == book.description
        assert retrieved_book.isbn == book.isbn

