from dataclasses import dataclass
from uuid import UUID

from src.domain.value_objects import FullName


@dataclass
class BaseDTO:
    ...


@dataclass
class AuthorInput(BaseDTO):
    fullname: FullName
    biography: str


@dataclass
class AuthorOutput(BaseDTO):
    id: UUID
    fullname: FullName
    biography: str

