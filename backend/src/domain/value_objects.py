from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject:
    ...


@dataclass(frozen=True)
class FullName(BaseValueObject):
    first_name: str
    last_name: str


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str


@dataclass(frozen=True)
class Description(BaseValueObject):
    value: str


@dataclass(frozen=True)
class ISBN(BaseValueObject):
    value: str

