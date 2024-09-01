import uuid
from sqlalchemy import ForeignKey, MetaData, Table, Column, UUID, String, Text, Boolean
from sqlalchemy.orm import backref, composite, registry, relationship

from src.domain.entities import Book, Author # pyright: ignore
from src.domain.value_objects import ISBN, Description, FullName, Title # pyright: ignore

metadata = MetaData()
mapper_registry = registry()


authors = Table(
    "authors", metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("first_name", String(20), nullable=False),
    Column("last_name", String(20), nullable=False),
    Column("biography", Text),
)

books = Table(
    "books", metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("book_title", String(64), nullable=False),
    Column("book_description", Text, nullable=False),
    Column("book_isbn", String(12), nullable=False),
    Column("is_available", Boolean, default=False),
    Column("filename", String(64), nullable=True),
)


author_book_table = Table(
    'book_authors', metadata,
    Column('book_id', UUID(as_uuid=True), ForeignKey('books.id'), primary_key=True),
    Column('author_id', UUID(as_uuid=True), ForeignKey('authors.id'), primary_key=True)
)


def start_mappers() -> None:
    authors_mapper = mapper_registry.map_imperatively(
        Author, authors, 
        properties = {
            "fullname": composite(FullName, authors.c.first_name, authors.c.last_name),
            "biography": authors.c.biography,
            "books": relationship(Book, secondary=author_book_table, back_populates="authors", collection_class=set)
        }
    )

    books_mapper = mapper_registry.map_imperatively(
        Book, books,
        properties = {
            "title": composite(Title, books.c.book_title),
            "description": composite(Description, books.c.book_description),
            "authors": relationship(Author, secondary=author_book_table, back_populates="books", collection_class=set),
            "isbn": composite(ISBN, books.c.book_isbn),
            "is_available": books.c.is_available,
            "filename": books.c.filename,
        }
    )

