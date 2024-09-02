from src.domain.entities import Author
from src.domain.value_objects import FullName
from src.infrastructure.persistence.repository import AuthorRepository
from tests.unit.common.fake_repository import List


class TestAuthorRepository:
    def test_create_repository(self, session) -> None:
        repository = AuthorRepository(session=session)
        
        assert isinstance(repository, AuthorRepository)

    def test_repository_can_create_author(self, session) -> None:
        fullname = FullName(first_name="John", last_name="Doe")
        author = Author(fullname=fullname, biography="A famous author")
        repository = AuthorRepository(session=session)

        repository.create(instance=author)
        retrieved_author = repository.get(key="id", value=author.id)

        assert isinstance(retrieved_author, Author)
        assert retrieved_author == author

    def test_repository_can_get_all_authors(self, session) -> None:
        author1 = Author(fullname=FullName(first_name="John", last_name="Doe"))
        author2 = Author(fullname=FullName(first_name="Jane", last_name="Smith"))
        repository = AuthorRepository(session=session)

        repository.create(instance=author1)
        repository.create(instance=author2)
        retrieved_authors = repository.all()
        
        expected = [author1, author2]
        assert isinstance(retrieved_authors, List)
        assert retrieved_authors == expected

    def test_repository_can_get_author_by_id(self, session) -> None:
        fullname = FullName(first_name="John", last_name="Doe")
        author = Author(fullname=fullname, biography="A famous author")
        repository = AuthorRepository(session=session)

        repository.create(instance=author)
        retrieved_author = repository.get_by_id(id=author.id)

        assert isinstance(retrieved_author, Author)
        assert retrieved_author == author


