from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any, Optional, List

from .entities import BaseEntity, Author, Book


T = TypeVar(name="T", bound=BaseEntity)


class AbstractRepository(ABC, Generic[T]):

    @abstractmethod
    def create(self, instance: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str, value: Any) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> List[T]:
        raise NotImplementedError


class AbstractAuthorRepository(AbstractRepository[Author], ABC):
    ...


class AbstractBookRepository(AbstractRepository[Book], ABC):
    ...

