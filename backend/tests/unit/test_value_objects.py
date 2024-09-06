import pytest
from src.domain.value_objects import FullName, Title, Description, ISBN


class FullName:
    def test_create_fullname(self) -> None:
        fullname = FullName(first_name="John", last_name="Doe")

        assert isinstance(fullname, FullName)
        assert fullname.fitst_name == "John"
        assert fullname.last_name == "Doe"

    def test_create_fullname_without_first_name_value_error(self) -> None:
        fullname = FullName(first_name="", last_name="Doe")

    def test_create_fullname_without_last_name_value_error(self) -> None:
        fullname = FullName(first_name="John", last_name="")


class TestTitle:
    def test_create_title(self) -> None:
        value = "Domain-Driven Design: Tackling Complexity in the Heart of Software" 
        title = Title(value=value)

        assert isinstance(title, Title)
        assert title.value == value

    def test_create_title_value_error(self) -> None:
        with pytest.raises(ValueError):
            title = Title(value = "a"*129)


class TestDescription:
    def test_create_description(self) -> None:
        value = "Book about Domain-Driven Design"  
        description = Description(value=value)
        
        assert isinstance(description, Description)
        assert description.value == value

    def test_create_description(self) -> None:
        with pytest.raises(ValueError):
            description = Description(value="a"*513)


class TestISBN:
    def test_create_isbn(self) -> None:
        value = "9780321125217"
        isbn = ISBN(value=value)

        assert isinstance(isbn, ISBN)
        assert isbn.value == value

    def test_create_isbn_longer_value_error(self) -> None:
        with pytest.raises(ValueError):
            isbn = ISBN(value="1"*14)

    def test_create_isbn_not_digit_value_error(self) -> None:
        with pytest.raises(ValueError):
            isbn = ISBN(value="wfh323of-asdf")

