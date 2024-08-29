from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar
from sqlalchemy.orm import Session
from src.domain.entities import Author # pyright: ignore
from src.domain.repository import AbstractRepository # pyright: ignore

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
        self, session: Session, repository: AbstractRepository
    ) -> None:
        self.session = session
        self.repository = repository

    def create(self, payload: AuthorInput) -> Optional[Author]:
        author = Author(**payload.__dict__)
        self.repository.create(instance=author)
        self.session.commit()
        
        return author

    def get(self, key: str, value: Any) -> Optional[Author]:
        return self.repository.get(key=key, value=value)  

    def all(self) -> Optional[List[Author]]:
        return self.repository.all()

