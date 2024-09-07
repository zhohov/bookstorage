from typing import Dict, Optional

from pytest import Session

from .session import DEFAULT_SESSION_FACTORY
from src.infrastructure.persistence.repository import AuthorRepository
from src.domain.repository import AbstractRepository
from src.domain.uow import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY) -> None:
        self.session_factory = session_factory

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        self.session: Session = self.session_factory()
        self.author_repository = AuthorRepository(session=self.session)
        return self

    def __exit__(self, exc_type: Optional[type[BaseException]], *args) -> None:
        if not exc_type:
            self.commit()
        else:
            self.rollback()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

