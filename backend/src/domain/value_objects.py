from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject:
    ...


@dataclass(frozen=True)
class FullName(BaseValueObject):
    first_name: str
    last_name: str

