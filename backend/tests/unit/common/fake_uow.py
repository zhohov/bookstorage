from typing import Optional
from src.domain.repository import AbstractRepository
from src.domain.uow import AbstractUnitOfWork
from .fake_repository import FakeAuthorRepository, FakeBookRepository


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self) -> None:
        self.commited = False
        self.author_repository = FakeAuthorRepository()
        self.book_repository = FakeBookRepository()

    def commit(self) -> None:
        self.commited = True

    def rollback(self) -> None:
        pass

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: Optional[type[BaseException]], *args) -> None:
        if not exc_type:
            self.commit()
        else:
            self.rollback()
