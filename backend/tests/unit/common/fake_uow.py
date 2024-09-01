from typing import Dict, Optional
from src.domain.repository import AbstractRepository
from src.domain.uow import AbstractUnitOfWork


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self, repositories: Dict[str, AbstractRepository]) -> None:
        self.commited = False
        self.repositories = repositories

    def get_repository(self, name: str) -> AbstractRepository:
        repository = self.repositories.get(name)
        if not repository:
            raise ValueError()
        return repository

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
