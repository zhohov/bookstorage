from abc import ABC, abstractmethod

from src.domain.repository import AbstractRepository


class AbstractUnitOfWork(ABC):
    @abstractmethod
    def __enter__(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def __exit__(self, exc_type: type[BaseException], *args) -> None:
        raise NotImplementedError

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_repository(self) -> AbstractRepository:
        raise NotImplementedError()
