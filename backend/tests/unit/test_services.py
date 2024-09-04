from typing import List

from src.domain.entities import Author
from src.domain.value_objects import FullName
from src.application.services.services import AuthorService

from src.application.dto.dto import AuthorInput

from .common.fake_repository import FakeAuthorRepository
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
    assert retrieved_author.fullname.first_name == author.fullname.first_name


def test_get_all_authors() -> None:
    uow = FakeUnitOfWork()
    service = AuthorService(uow=uow)
    fullname = FullName(first_name="John", last_name="Doe")
    payload = AuthorInput(fullname=fullname, biography="A famous author")

    author = service.create(payload=payload)
    retrieved_authors = service.all()

    expected = [author]

    assert isinstance(retrieved_authors, List)
    assert retrieved_authors == expected
    
