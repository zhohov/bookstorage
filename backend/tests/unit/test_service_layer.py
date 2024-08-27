from typing import List

from src.domain.entities import Author
from src.domain.value_objects import FullName
from src.infrastructure.database.repository import FakeAuthorRepository
from src.application.services.services import AuthorService


def test_create_author(fake_session) -> None:
    repository = FakeAuthorRepository()
    service = AuthorService(session=fake_session, repository=repository)
    fullname = FullName(first_name="John", last_name="Doe")
    payload = AuthorInput(fullname=fullname, biography="A famous author")

    author = service.create(payload=payload)
    retrieved_author = service.get(key="id", value=author.id)

    assert isinstance(author, Author)
    assert retrieved_author.id == author.id
    assert retrieved_author.fullname.first_name == author.fullname.first_name


def test_get_all_authors(fake_session) -> None:
    repository = FakeAuthorRepository()
    service = AuthorService(session=fake_session, repository=repository)
    fullname = FullName(first_name="John", last_name="Doe")
    payload = AuthorInput(fullname=fullname, biography="A famous author")


    author = service.create(payload=payload)
    retrieved_authors = service.all()

    expected = [author]

    assert isinstance(retrieved_authors, List)
    assert retrieved_authors == expected
    
