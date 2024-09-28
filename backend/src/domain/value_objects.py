from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject:
   ...


@dataclass(frozen=True)
class FullName(BaseValueObject):
    first_name: str
    last_name: str

    def validate_length(self, value: str) -> None:
        if len(value) > 64 or len(value) < 3:
            raise ValueError()

    def validate(self) -> None:
        self.validate_length(value=self.first_name)
        self.validate_length(value=self.last_name)

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
        if len(self.value) > 13 or not self.value.isdigit():
            raise ValueError()

    def __post_init__(self) -> None:
        self.validate()

