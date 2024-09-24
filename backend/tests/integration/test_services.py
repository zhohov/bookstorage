from src.infrastructure.persistence.repository import AuthorRepository
from src.infrastructure.persistence.uow import SqlAlchemyUnitOfWork
from src.application.services.services import AuthorService

from src.application.dto.dto import AuthorInput
from src.domain.value_objects import FullName
from src.domain.entities import Author
from tests.conftest import session_factory


class TestAuthorService:
    def test_create_author(self, session_factory) -> None:
        uow = SqlAlchemyUnitOfWork(session_factory=session_factory)
        service = AuthorService(uow=uow)
        fullname = FullName(first_name="John", last_name="Doe")
        payload = AuthorInput(fullname=fullname, biography="A famous author")

        author = service.create(payload=payload)
        retrieved_author = service.get(key="id", value=author.id)

        assert isinstance(author, Author)
        assert retrieved_author.id == author.id
        assert retrieved_author.fullname["first_name"] == author.fullname.first_name

