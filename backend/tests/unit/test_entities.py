from src.domain.entities import Author, Book
from src.domain.value_objects import FullName, Title, Description, ISBN


def create_author() -> Author:
    fullname = FullName(first_name="Eric", last_name="Evans")
    author = Author(fullname=fullname)
    return author


def create_book() -> Book:
    title = Title(value="Domain-Driven Design: Tackling Complexity in the Heart of Software")
    description = Description(value="Book about Domain-Driven Design")
    isbn = ISBN(value="9780321125217")

    book = Book(title=title, description=description, isbn=isbn)
    
    return book


def test_create_book_without_author() -> None:
    title = Title(value="Domain-Driven Design: Tackling Complexity in the Heart of Software")
    description = Description(value="Book about Domain-Driven Design")
    isbn = ISBN(value="9780321125217")

    book = Book(title=title, description=description, isbn=isbn)

    assert book.title == title
    assert book.description == description
    assert book.isbn == isbn
    assert book.authors == set()
    assert book.is_available == False
    assert book.filename == None


def test_add_author_in_book() -> None:
    author: Author = create_author()
    book = create_book()

    book.add_author(author=author)

    assert book.authors == set([author])


def test_update_availability() -> None:
    book:  Book = create_book()
    book.update_availability(value=True)
    
    assert book.is_available == True


def test_update_filename() -> None:
    book:  Book = create_book()
    book.update_filename(value="domain_driven_design")

    assert book.filename == "domain_driven_design"


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




