from src.domain.entities import Author
from src.domain.value_objects import FullName


def test_succesful_create_author_without_biography() -> None:
    fullname = FullName(first_name="Eric", last_name="Evans")
    author = Author(fullname=fullname)

    assert author.fullname == fullname
    assert author.biography == None


def test_succesful_create_author_with_biography() -> None:
    fullname = FullName(first_name="Eric", last_name="Evans")
    biography = "Eric Evans biography"
    author = Author(fullname=fullname, biography=biography)

    assert author.fullname == fullname
    assert author.biography == biography

