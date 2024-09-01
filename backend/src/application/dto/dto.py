from dataclasses import dataclass

from src.domain.value_objects import FullName # pyright: ignore


@dataclass
class BaseDTO:
    ...


@dataclass
class AuthorInput(BaseDTO):
    fullname: FullName
    biography: str

