import uuid
from typing import Any, Generic, List, TypeVar, Optional
from sqlalchemy import Result, select
from src.domain.entities import BaseEntity, Author, Book
from src.domain.repository import AbstractRepository, AbstractAuthorRepository

from sqlalchemy.orm import Session


T = TypeVar("T", bound=BaseEntity)


class SqlAlchemyRepository(AbstractRepository[T], Generic[T]):
    def __init__(self, session: Session, entity: type[T]) -> None:
        self.session = session
        self.entity = entity

    def create(self, instance: T) -> None:
        self.session.add(instance)

    def get(self, key: str, value: Any) -> Optional[T]:
        query = select(self.entity).where(
            getattr(self.entity, key) == value,
        )
        result: Result = self.session.execute(statement=query)

        return result.scalars().one_or_none()

    def all(self) -> Optional[List[T]]:
        query = select(self.entity)
        result: Result = self.session.execute(statement=query)
        return result.scalars().all()


class AuthorRepository(SqlAlchemyRepository[Author], AbstractAuthorRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, entity=Author)

    def get_by_id(self, id: uuid.uuid4) -> Optional[Author]:
        return self.get(key="id", value=id)


class BookRepository(SqlAlchemyRepository[Book], AbstractAuthorRepository):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, entity=Book)
