from dataclasses import dataclass

from src.domain.value_objects import FullName # pyright: ignore


@dataclass
class AuthorInput:
    fullname: FullName
    biography: str

