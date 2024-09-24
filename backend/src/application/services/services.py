from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar
from uuid import UUID

from sqlalchemy import except_
from src.domain.repository import AbstractAuthorRepository
from src.infrastructure.persistence.repository import AuthorRepository
from src.domain.uow import AbstractUnitOfWork
from src.domain.entities import Author # pyright: ignore

from src.application.dto.dto import BaseDTO, AuthorInput, AuthorOutput


T = TypeVar("T", bound=BaseDTO)


class AbstractService(ABC, Generic[T]):
    @abstractmethod
    def create(self, payload: T) -> Optional[T]:
        ...

    @abstractmethod
    def get(self, key: str, value: Any) -> Optional[T]:
        ...

    @abstractmethod
    def all(self) -> Optional[List[T]]:
        ...


class AuthorService(AbstractService[T]):
    def __init__(
        self, uow: AbstractUnitOfWork
    ) -> None:
        self.uow = uow

    def create(self, payload: AuthorInput) -> Optional[Author]:
        author = Author(**payload.__dict__)

        with self.uow:
            repository: AbstractAuthorRepository = self.uow.author_repository
            repository.create(instance=author)
        
        return author

    def get(self, key: str, value: Any) -> Optional[AuthorOutput]:
        with self.uow:
            repository: AbstractAuthorRepository = self.uow.author_repository
            retrieved_author = repository.get(key=key, value=value)
            author = AuthorOutput(**retrieved_author.to_dict())
            return author  

    def all(self) -> Optional[List[AuthorOutput]]:
        with self.uow:
            repository: AbstractAuthorRepository = self.uow.author_repository
            authors = repository.all()
            result = [AuthorOutput(**author.to_dict()) for author in authors]
            return result

    def get_by_id(self, id: UUID) -> Optional[AuthorOutput]:
        with self.uow:
            repository: AbstractAuthorRepository = self.uow.author_repository
            try:
                retrieved_author = repository.get_by_id(id=id)
                author = AuthorOutput(**retrieved_author.to_dict())
                return author
            except ValueError:
                return None

