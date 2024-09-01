from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar
from src.domain.uow import AbstractUnitOfWork
from src.domain.entities import Author # pyright: ignore

from src.application.dto.dto import BaseDTO, AuthorInput # pyright: ignore


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
            repository = self.uow.get_repository(name="AuthorRepository")
            repository.create(instance=author)
        
        return author

    def get(self, key: str, value: Any) -> Optional[Author]:
        with self.uow:
            repository = self.uow.get_repository(name="AuthorRepository")
            return repository.get(key=key, value=value)  

    def all(self) -> Optional[List[Author]]:
        with self.uow:
            repository = self.uow.get_repository(name="AuthorRepository")
            return repository.all()

