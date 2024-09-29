from dataclasses import dataclass
from uuid import UUID

from src.domain.value_objects import ISBN, Description, FullName, Title


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

@dataclass
class BookInput(BaseDTO):
    title: Title
    description: Description
    isbn: ISBN


@dataclass
class BookOutput(BaseDTO):
    id: UUID
    title: Title
    description: Description
    isbn: ISBN

