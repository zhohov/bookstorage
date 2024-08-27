from typing import Any, List, Optional, Dict
from sqlalchemy.orm import Session
from src.domain.entities import Author # pyright: ignore
from src.domain.repository import AbstractRepository # pyright: ignore

from src.application.dto.dto import AuthorInput # pyright: ignore


class AuthorService:
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

