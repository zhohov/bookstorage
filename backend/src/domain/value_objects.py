from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject:
    ...


@dataclass(frozen=True)
class FullName(BaseValueObject):
    first_name: str
    last_name: str

    def validate(self) -> None:
        if len(self.first_name) > 64 or len(self.last_name) > 64:
            raise ValueError()

    def __post_init__(self) -> None:
        self.validate()


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self) -> None:
        if len(self.value) > 128:
            raise ValueError()

    def __post_init__(self) -> None:
        self.validate()


@dataclass(frozen=True)
class Description(BaseValueObject):
    value: str

    def validate(self) -> None:
        if len(self.value) > 512:
            raise ValueError()

    def __post_init__(self) -> None:
        self.validate()


@dataclass(frozen=True)
class ISBN(BaseValueObject):
    value: str

    def validate(self) -> None:
        if len(self.value) > 13 or not self.value.isdigit:
            raise ValueError()

    def __post_init__(self) -> None:
        self.validate()

