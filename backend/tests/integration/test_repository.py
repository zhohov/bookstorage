from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, ISBN, Title, Description
from src.infrastructure.persistence.repository import AuthorRepository, BookRepository
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


class TestBookRepository:
    def test_create_repository(self, session) -> None:
        repository = BookRepository(session=session)
        
        assert isinstance(repository, BookRepository)

    def test_repository_can_create_author(self, session) -> None:
        title = Title(value="Domain-Driven Design: Tackling Complexity in the Heart of Software")
        description = Description(value="Book about Domain-Driven Design")
        isbn = ISBN(value="9780321125217")
        book = Book(title=title, description=description, isbn=isbn)
        repository = BookRepository(session=session)

        repository.create(instance=book)
        retrieved_author = repository.get(key="id", value=book.id)

        assert isinstance(retrieved_author, Book)
        assert retrieved_author == book

