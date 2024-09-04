from typing import Dict, Optional

from sqlalchemy.orm import Session
from src.infrastructure.persistence.repository import AuthorRepository
from src.domain.repository import AbstractRepository
from src.domain.uow import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Session) -> None:
        self.session = session
        self.author_repository = AuthorRepository(session=session)

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
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

