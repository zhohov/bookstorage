import uuid
from typing import Optional

from .value_objects import FullName


class BaseEntity:
    def __init__(self) -> None:
        self.id = uuid.uuid4()


class Author(BaseEntity):
    def __init__(
        self, fullname: FullName, biography: Optional[str] = None
    )-> None:
        super().__init__()
        self.fullname = fullname
        self.biography = biography

    def __eq__(self, other) -> bool:
        if not isinstance(other, Author):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

