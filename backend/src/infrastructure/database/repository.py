from typing import Any, List, Optional, Set, TypeVar, Generic

from src.domain.entities import BaseEntity, Author, Book # pyright: ignore
from src.domain.repository import AbstractRepository, AbstractAuthorRepository, AbstractBookRepository # pyright: ignore


T = TypeVar(name="T", bound=BaseEntity)


class FakeRepository(AbstractRepository[T], Generic[T]):
    def __init__(self, entity: type[T]) -> None:
        self.entity = entity
        self.instances: Set[T] = set()

    def create(self, instance: T) -> None:
        self.instances.add(instance)

    def get(self, key: str, value: Any) -> Optional[T]:
        for instance in self.instances:
            if getattr(instance, key) == value:
                return instance

        raise ValueError()

    def all(self) -> Optional[List[T]]:
        if not self.instances:
            raise ValueError()

        return [instance for instance in self.instances]


class FakeAuthorRepository(FakeRepository[Author], AbstractAuthorRepository):
    def __init__(self, ) -> None:
        super().__init__(entity=Author)


class FakeBookRepository(FakeRepository[Book], AbstractBookRepository):
    def __init__(self, ) -> None:
        super().__init__(entity=Book)
    
